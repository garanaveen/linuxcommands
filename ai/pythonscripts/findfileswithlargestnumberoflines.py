import os

def count_lines_in_file(file_path):
    """Counts the number of lines in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return sum(1 for _ in file)
    except Exception as e:
        print(f"Could not read file {file_path}: {e}")
        return 0

def find_and_sort_files_by_lines(start_dir):
    """Finds all files under the given directory and sorts them by line count."""
    file_line_counts = []

    for root, _, files in os.walk(start_dir):
        for file in files:
            file_path = os.path.join(root, file)
            line_count = count_lines_in_file(file_path)
            file_line_counts.append((file_path, line_count))

    # Sort files by line count in ascending order
    file_line_counts.sort(key=lambda x: x[1])

    return file_line_counts

if __name__ == "__main__":
    start_directory = os.getcwd()  # Start from the current directory
    sorted_files = find_and_sort_files_by_lines(start_directory)

    print("Files sorted by number of lines:")
    for file_path, line_count in sorted_files:
        print(f"{file_path}: {line_count} lines")
