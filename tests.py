from functions.get_files_info import get_files_info, get_file_content, write_file

if __name__ == "__main__":
    print("Test 1: write_file('calculator', 'lorem.txt', 'wait, this isn't lorem ipsum'")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

    print("\nTest 2: write_file('calculator', 'pkg/morelorem.txt', 'lorem ipsum dolor sit amet')")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

    print("\nTest 3: write_file('calculator', '/tmp/temp.txt', 'this should not be allowed')")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))  # Expecting error