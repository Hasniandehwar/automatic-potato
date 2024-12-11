
from Book import Books       # view_books, borrow_book, return_book
from Bowrrow_r import Borrow_return
class Member_menu:
    def member_menu():
        print("\nWelcome to the Member Panel")
        while True:
            print("\nMember Menu:")
            print("1. View Books")
            print("2. Borrow Book")
            print("3. Return Book")
            print("4. Exit to Main Menu")

            choice = input("Enter your choice: ")

        # Input validation for member menu
            if not choice.isdigit() or int(choice) not in [1, 2, 3, 4]:
                print("Invalid choice. Please enter a valid option.")
                continue

            if choice == "1":
                books = Books()
                books.view_books()

            elif choice == "2":
                Borrow_return().borrow_book()

            elif choice == "3":
                Borrow_return().return_book()

            elif choice == "4":
                 print("Exiting Member Panel.")
                 break

