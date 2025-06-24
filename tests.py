from functions.get_files_info import get_files_info

if __name__ == "__main__":
    print("Test 1: get_files_info('calculator', '.')")
    print(get_files_info("calculator", "."))

    print("\nTest 2: get_files_info('calculator', 'pkg')")
    print(get_files_info("calculator", "pkg"))

    print("\nTest 3: get_files_info('calculator', '/bin')")
    print(get_files_info("calculator", "/bin"))  # Expecting error

    print("\nTest 4: get_files_info('calculator', '../')")
    print(get_files_info("calculator", "../"))   # Expecting error