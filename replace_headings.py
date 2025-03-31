import re

def replace_headings(html):
    # Replace opening heading tags
    html = re.sub(r'<h([1-6])>(.*?)</h\1>', r'<p class="heading h\1">\2</p>', html, flags=re.DOTALL)

    return html

def process_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    updated_html = replace_headings(html_content)

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(updated_html)

    print(f"Replaced headings saved to {output_path}")

# Example usage
if __name__ == "__main__":
    input_file = 'index.html'
    output_file = 'index.html'
    process_file(input_file, output_file)
