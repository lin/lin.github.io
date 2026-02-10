from bs4 import BeautifulSoup
import os
import re

base_dir = '/Users/albert/Documents/Projects/lin.github.io/static/xiaonei'
index_path = os.path.join(base_dir, 'index.html')
style_path = os.path.join(base_dir, 'style.css')

# 1. Process style.css to comment out @import
with open(style_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Comment out @import lines
css_content = re.sub(r'(@import url\(.*?\);)', r'/* \1 */', css_content)

with open(style_path, 'w', encoding='utf-8') as f:
    f.write(css_content)
print("Updated style.css")

# 2. Process index.html
with open(index_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Remove scripts
for script in soup.find_all('script'):
    script.decompose()

# Remove links
for link in soup.find_all('link'):
    link.decompose()

# Add new CSS link
head = soup.head
new_link = soup.new_tag('link', rel='stylesheet', href='style.css')
head.append(new_link)

# Empty talk div
talk_div = soup.find('div', id='talk')
if talk_div:
    talk_div.clear()
else:
    print("Warning: <div id='talk'> not found")

# Empty pager-top
pager_div = soup.find('div', class_='pager-top')
if pager_div:
    pager_div.clear()
    # Add a placeholder for dynamic pager if needed, or just let JS handle it
    pager_div['id'] = 'pagination' 

# Add JS
js_content = """
async function loadPosts() {
    const urlParams = new URLSearchParams(window.location.search);
    const page = parseInt(urlParams.get('page')) || 1;
    const filename = `posts_${page}.txt`;
    const fetchUrl = `${filename}?t=${new Date().getTime()}`;

    try {
        const response = await fetch(fetchUrl);
        if (!response.ok) {
             if(response.status === 404) {
                 document.getElementById('talk').innerHTML = '<div style="padding:20px; text-align:center;">没有更多留言了 (No more posts)</div>';
                 return;
             }
             throw new Error('Failed to load posts');
        }
        const text = await response.text();
        const talkDiv = document.getElementById('talk');
        talkDiv.innerHTML = '';

        const rawPosts = text.split('————').map(p => p.trim()).filter(p => p);

        rawPosts.forEach(rawPost => {
            const lines = rawPost.split('\\n').map(l => l.trim()).filter(l => l);
            if (lines.length === 0) return;
            
            const metaLine = lines.pop();
            const content = lines.join('<br>');
            
            let author = '';
            let time = '';
            
            // Format: Time Author
            // e.g. "11-12 22:10 林英魁"
            const parts = metaLine.split(' ');
            if (parts.length >= 2) {
                author = parts.pop();
                time = parts.join(' ');
            } else {
                time = metaLine;
            }

            const commentDiv = document.createElement('div');
            commentDiv.className = 'comment';
            
            // Use a default avatar
            const imgUrl = 'http://xnimg.cn/imgpro/icons/statusface/1.gif'; 
            
            commentDiv.innerHTML = `
                <div class="actor-img">
                    <img src="${imgUrl}" style="width:50px; height:50px; background:#eee; border:1px solid #ccc;"> 
                </div>
                <div class="cmt-body">
                    <div class="info">
                        <span class="author"><a href="#">${author}</a></span>
                        <span class="time" style="color:#999; margin-left:10px;">${time}</span>
                    </div>
                    <div class="text-content" style="margin-top:5px;">${content}</div>
                </div>
            `;
            talkDiv.appendChild(commentDiv);
        });
        
        // Update Pagination
        const paginationDiv = document.getElementById('pagination');
        if (paginationDiv) {
            paginationDiv.innerHTML = '';
            const ol = document.createElement('ol');
            ol.className = 'pagerpro';
            
            // Simple Prev/Next
            if (page > 1) {
                const prevLi = document.createElement('li');
                prevLi.innerHTML = `<a href="?page=${page - 1}">上一页</a>`;
                ol.appendChild(prevLi);
            }
            
            const currentLi = document.createElement('li');
            currentLi.className = 'current';
            currentLi.innerHTML = `<a href="#">${page}</a>`;
            ol.appendChild(currentLi);
            
            const nextLi = document.createElement('li');
            nextLi.innerHTML = `<a href="?page=${page + 1}">下一页</a>`;
            ol.appendChild(nextLi);
            
            paginationDiv.appendChild(ol);
        }

    } catch (error) {
        console.error(error);
        document.getElementById('talk').innerHTML = '<div style="padding:20px">Error loading posts.</div>';
    }
}

document.addEventListener('DOMContentLoaded', loadPosts);
"""

script_tag = soup.new_tag('script')
script_tag.string = js_content
soup.body.append(script_tag)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Updated index.html")
