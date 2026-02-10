import os
import re
import email
from email import policy
from bs4 import BeautifulSoup
import glob

SOURCE_DIR = '/Users/albert/Documents/Projects/lin.github.io/static/xiaonei'
OUTPUT_DIR = SOURCE_DIR

def extract_posts_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    comments = soup.find_all('div', class_='comment')
    posts = []
    
    for comment in comments:
        author_span = comment.find('span', class_='author')
        author = author_span.get_text(strip=True) if author_span else "Unknown"
        
        time_span = comment.find('span', class_='time')
        time_str = time_span.get_text(strip=True) if time_span else ""
        
        content_div = comment.find('div', class_='text-content')
        content = content_div.get_text('\n', strip=True) if content_div else ""
            
        posts.append({
            'content': content,
            'author': author,
            'time': time_str
        })
    return posts

def extract_posts_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    posts = []
    current_post = None
    
    # Regex to match "Author Time" line
    # e.g. "韩龙 11-28 16:27" or "林英魁 11-28 13:02"
    header_pattern = re.compile(r'^(.*?) (\d{2}-\d{2} \d{2}:\d{2})\s*$')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        match = header_pattern.match(line)
        if match:
            # If we have a current post accumulating, save it
            if current_post:
                posts.append(current_post)
            
            # Start new post
            current_post = {
                'author': match.group(1),
                'time': match.group(2),
                'content_lines': []
            }
        else:
            if current_post:
                # Skip "回复" or "删除" lines if they are exact matches
                if line in ['回复', '删除']:
                    continue
                current_post['content_lines'].append(line)
    
    # Append the last post
    if current_post:
        posts.append(current_post)
    
    # Format for output
    formatted_posts = []
    for p in posts:
        formatted_posts.append({
            'content': "\n".join(p['content_lines']),
            'author': p['author'],
            'time': p['time']
        })
        
    return formatted_posts

def process_mht(file_path):
    try:
        with open(file_path, 'rb') as f:
            msg = email.message_from_binary_file(f, policy=policy.default)
        
        html_content = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/html':
                    try:
                        html_content = part.get_content()
                        break
                    except Exception as e:
                        print(f"Error getting content from part: {e}")
        else:
            if msg.get_content_type() == 'text/html':
                html_content = msg.get_content()
                
        return html_content
    except Exception as e:
        print(f"Error processing MHT {file_path}: {e}")
        return None

def process_files():
    # Find all relevant files
    files = glob.glob(os.path.join(SOURCE_DIR, '校内网 - 我的留言板*'))
    
    # Filter and sort files by their page number
    # We prioritize .mht, then .txt. We ignore .doc if .txt exists.
    files_map = {} # page_id -> file_info
    
    for file_path in files:
        filename = os.path.basename(file_path)
        match = re.search(r'校内网 - 我的留言板(\d+)\.(mht|doc|txt)', filename)
        if match:
            page_id = int(match.group(1))
            ext = match.group(2).lower()
            
            if page_id not in files_map:
                files_map[page_id] = {'path': file_path, 'ext': ext, 'filename': filename}
            else:
                # If we already have an entry, prefer MHT over TXT over DOC
                current_ext = files_map[page_id]['ext']
                if ext == 'mht':
                    files_map[page_id] = {'path': file_path, 'ext': ext, 'filename': filename}
                elif ext == 'txt' and current_ext != 'mht':
                     files_map[page_id] = {'path': file_path, 'ext': ext, 'filename': filename}
    
    # Sort by original page ID
    sorted_page_ids = sorted(files_map.keys())
    
    for page_id in sorted_page_ids:
        file_info = files_map[page_id]
        print(f"Processing page {page_id} ({file_info['filename']})...")
        
        posts = []
        if file_info['ext'] == 'mht':
            html_content = process_mht(file_info['path'])
            if html_content:
                posts = extract_posts_from_html(html_content)
        elif file_info['ext'] == 'txt':
             posts = extract_posts_from_txt(file_info['path'])
        elif file_info['ext'] == 'doc':
            print(f"Skipping binary .doc file {file_info['filename']} (provide .txt version if needed)")
            continue
            
        if posts:
            # Output file matches the original page ID directly
            output_path = os.path.join(OUTPUT_DIR, f'posts_{page_id}.txt')
            with open(output_path, 'w', encoding='utf-8') as f:
                for post in posts:
                    f.write(f"{post['content']}\n")
                    f.write(f"{post['time']} {post['author']}\n")
                    f.write("————\n")
            print(f"Saved {len(posts)} posts to {output_path}")
        else:
            print(f"No posts found or skipped for {file_info['filename']}")

if __name__ == '__main__':
    process_files()
