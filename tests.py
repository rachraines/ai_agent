from functions.get_files_info import get_files_info, get_file_content, write_file, run_python_file

if __name__ == "__main__":
    print("Test 1: run_python_file('calculator', 'main.py'")
    print(run_python_file("calculator", "main.py"))

    print("\nTest 2: run_python_file('calculator', 'tests.py'")
    print(run_python_file("calculator", "tests.py"))

    print("\nTest 3: run_python_file('calculator', '../main.py'")
    print(run_python_file("calculator", "../main.py"))  # Expecting error

    print("\nTest 4: run_python_file('calculator', 'nonexistent.py'")
    print(run_python_file("calculator", "nonexistent.py"))  # Expecting error