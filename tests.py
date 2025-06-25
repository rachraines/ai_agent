from functions.get_files_info import get_files_info, get_file_content

if __name__ == "__main__":
    print("Test 1: get_file_content('calculator', 'main.py')")
    print(get_file_content("calculator", "main.py"))

    print("\nTest 2: get_file_content('calculator', 'pkg/calculator.py')")
    print(get_file_content("calculator", "pkg/calculator.py"))

    print("\nTest 3: get_file_content('calculator', '/bin/cat')")
    print(get_file_content("calculator", "/bin/cat"))  # Expecting error