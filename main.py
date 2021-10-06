import Task1
import Task2
import Task3

def main():
    print("*Task 1*")
    Task1.convert_json_files_to_dictionaries()
    Task1.uniform_cost_search_1("1", "50")
    print()

    print("*Task 2*")
    Task2.convert_json_files_to_dictionaries()
    Task2.uniform_cost_search_2("1", "50", 287932)
    print()

    print("*Task 3*")
    Task3.convert_json_files_to_dictionaries()
    Task3.a_star_search("1", "50", 287932)
    print()


if __name__ == "__main__":
    main()