
from members import Members  # Add_member, Remove_member, View_member
from Book import Books       # add_Book, update_books, Delete_book, count__book, view_books
class Admin:
    def admin_menu():
        print("\nWelcome to the Admin Panel")
        while True:
            print("\nAdmin Menu:")
            print("1. Manage Members")
            print("2. Manage Books")
            print("3. Exit to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                members = Members()
                print("\nMembers Management:")
                print("1. Add Member")
                print("2. Remove Member")
                print("3. View Members")
                choice = input("Enter your choice: ")
                if choice == "1":
                    members.Add_member()
                elif choice == "2":
                    members.Remove_member()
                elif choice == "3":
                    members.View_member()
                else:
                    print("Invalid choice.")

            elif choice == "2":
                books = Books()
                print("\nBooks Management:")
                print("1. Add Book")
                print("2. Update Book")
                print("3. Delete Book")
                print("4. View Books")
                print("5. Count Books")
                sub_choice = input("Enter your choice: ")
                if sub_choice == "1":
                    books.add_Book()
                elif sub_choice == "2":
                    books.update_books()
                elif sub_choice == "3":
                    books.Delete_book()
                elif sub_choice == "4":
                    books.view_books()
                elif sub_choice == "5":
                    books.count__book()
                else:
                    print("Invalid choice.")

            elif choice == "3":
                    print("Exiting Admin Panel.")
                    break

            else:
                print("Invalid choice. Please try again.")
