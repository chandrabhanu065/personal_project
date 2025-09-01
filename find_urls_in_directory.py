import os
import re


def find_urls_in_file(file_path):
    # Regular expression to find URLs
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    urls = []

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                urls.extend(url_pattern.findall(line))
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")

    return urls


def find_urls_in_directory(directory):
    all_urls = []

    # Walk through the directory using os.walk()
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)

            # Check for readable text files (you can adjust this if needed)
            if filename.endswith(('.txt', '.log', '.html', '.md', '.csv', '.json', '.py')):
                print(f"Scanning: {file_path}")
                urls = find_urls_in_file(file_path)
                if urls:
                    print(f"Found {len(urls)} URLs in {file_path}")
                    all_urls.extend(urls)

    return all_urls


# Example usage
directory_path = '/path/to/your/directory'
urls_found = find_urls_in_directory(directory_path)

print("\nAll URLs Found:")
for url in urls_found:
    print(url)
