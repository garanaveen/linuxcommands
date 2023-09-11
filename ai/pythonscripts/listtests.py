import os
import re

# Regular expression pattern to match class and test method definitions
class_pattern = re.compile(r"class (\w+)\(.*\):")
test_method_pattern = re.compile(r"def test_(\w+)\(self\):")

# Dictionary to store test methods by class
test_methods_by_class = {}

# Function to process a Python file
def process_python_file(file_path):
    current_class = None

    with open(file_path, "r") as file:
        for line in file:
            print("line:", line)
            print("---------")
            class_match = class_pattern.match(line)
            if class_match:
                current_class = class_match.group(1)
                print("current_class", current_class)
                test_methods_by_class[current_class] = []
            elif current_class:
                print("elif current_class:")
                test_match = test_method_pattern.match(line)
                if test_match:
                    test_name = test_match.group(1)
                    print("current_class", current_class)
                    test_methods_by_class[current_class].append(test_name)

# Walk through all .py files in the current directory and subdirectories
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            print("file_path", file_path)
            process_python_file(file_path)

# Print the test methods by class
for class_name, test_methods in test_methods_by_class.items():
    for test_method in test_methods:
        print(f"{class_name}.{test_method}")

