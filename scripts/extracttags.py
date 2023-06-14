import os
import re
import sys

def extract_hashtags(text):
    hashtags = re.findall(r'#([A-Za-z0-9]+)', text)
    return hashtags

def find_tags(directory):
    tags = set()

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath) and not (filepath.endswith('.log') or filename == 'tags.txt'):
            with open(filepath, 'r') as file:
                content = file.read()
                extracted_tags = extract_hashtags(content)
                tags.update(extracted_tags)

    return tags

def write_tags_to_file(tags, output_file):
    with open(output_file, 'w') as file:
        for tag in tags:
            file.write(f'{tag}\n')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    output_file = 'tags.txt'

    tags = find_tags(directory)
    write_tags_to_file(tags, output_file)

    print(f'Tags have been extracted and saved to {output_file}.')

