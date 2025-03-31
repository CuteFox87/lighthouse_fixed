import re
import os

def replace_img_extensions(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace jpg and png extensions with webp in img tags
    updated_content = re.sub(r'(<img[^>]+src="[^"]+)\.(jpg|png)"', r'\1.webp"', content, flags=re.IGNORECASE)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

# Example usage
for i in os.listdir('.'):
    if i.endswith('.html'):
        html_file_path = os.path.join('.', i)
        print(f"Processing file: {html_file_path}")
        replace_img_extensions(html_file_path)
        print(f"Updated file: {html_file_path}")