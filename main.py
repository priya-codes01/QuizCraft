from tv_quiz import run_tv_quiz
from cricket_quiz import run_cricket_quiz
from maths_quiz import run_maths_quiz


def main():
    while True:
        print("\nMain Menu")
        print("1. TV quiz")
        print("2. Indian cricket quiz")
        print("3. Maths quiz")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            run_tv_quiz()
        elif choice == "2":
            run_cricket_quiz()
        elif choice == "3":
            run_maths_quiz()
        elif choice == "4" or choice.lower() == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
