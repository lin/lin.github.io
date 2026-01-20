import os
import json

def generate_map():
    # Get all files in the current directory
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    image_map = {}

    for filename in files:
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
            # Remove extension
            name_without_ext = os.path.splitext(filename)[0]
            
            # Strategy: Split by '-' and check first part
            parts = name_without_ext.split('-')
            possible_id = parts[0]
            
            # Verify if it looks like a tweet ID (numeric)
            if possible_id.isdigit():
                if possible_id not in image_map:
                    image_map[possible_id] = []
                image_map[possible_id].append(filename)
    
    # Sort images for consistency
    for tid in image_map:
        image_map[tid].sort()

    # Write to images.json
    with open('images.json', 'w') as f:
        json.dump(image_map, f, indent=2)
    
    print(f"Generated images.json with {len(image_map)} tweets mapped.")

if __name__ == "__main__":
    generate_map()
