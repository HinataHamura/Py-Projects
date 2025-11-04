class LibraryItem:
    def __init__(self, title):
        self.title = title


class Book(LibraryItem):
    def __init__(self, id, title, author):
        super().__init__(title)
        self.id = id
        self.author = author
        self.available = True


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.next_book_id = 1

    def add_book(self, title, author):
        book = Book(self.next_book_id, title, author)
        self.books.append(book)
        self.next_book_id += 1
        return book

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        for book in self.books:
            availability = "Available" if book.available else "Not Available"
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Availability: {availability}")

    def search_book_by_name(self, name):
        found_books = [book for book in self.books if name.lower() in book.title.lower()]
        if found_books:
            print("Found books matching the search query:")
            for book in found_books:
                availability = "Available" if book.available else "Not Available"
                print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Availability: {availability}")
        else:
            print("No books found with the given name.")

    def display_members(self):
        if not self.members:
            print("No members in the library.")
            return
        print("List of current members:")
        for member in self.members:
            print(f"ID: {member.member_id}, Name: {member.name}")

    def add_member(self, name):
        member_id = len(self.members) + 1  # Generating unique member ID
        member = Member(member_id, name)
        self.members.append(member)
        return member

    def search_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                print(f"Member found: ID: {member.member_id}, Name: {member.name}")
                return member
        print("Member not found.")
        return None

    def borrow_book(self, member_id, book_id):
        member = self.search_member_by_id(member_id)
        if not member:
            print("Cannot borrow book. Member not found.")
            return
        book = self.find_book_by_id(book_id)
        if not book:
            print("Cannot borrow book. Book not found.")
            return
        if not book.available:
            print("Sorry, the book is not available for borrowing.")
            return
        member.borrowed_books.append(book)
        book.available = False
        print(f"Book '{book.title}' borrowed successfully by {member.name}.")

    def return_book(self, member_id, book_id):
        member = self.search_member_by_id(member_id)
        if not member:
            print("Cannot return book. Member not found.")
            return
        for book in member.borrowed_books:
            if book.id == book_id:
                book.available = True
                member.borrowed_books.remove(book)
                print(f"Book '{book.title}' returned successfully by {member.name}.")
                return
        print("Cannot return book. Book not found in the member's borrowed list.")

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None


def main():
    library = Library()

    # Adding some initial book and member data for testing
    library.add_book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("1984", "George Orwell")
    library.add_book("Pride and Prejudice", "Jane Austen")

    library.add_member("John Doe")
    library.add_member("Jane Smith")
    library.add_member("Alice Johnson")
    library.add_member("Bob Brown")
    library.add_member("Emma Davis")

    while True:
        print("\nMain Menu:")
        print("1. Show book collection")
        print("2. Add book")
        print("3. Search book by book name")
        print("4. Show list of current members")
        print("5. Add new member")
        print("6. Search member by member id")
        print("7. Borrow book")
        print("8. Return book")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            new_book = library.add_book(title, author)
            print(f"Book '{new_book.title}' added with ID {new_book.id}.")
        elif choice == "3":
            name = input("Enter the name of the book to search: ")
            library.search_book_by_name(name)
        elif choice == "4":
            library.display_members()
        elif choice == "5":
            name = input("Enter the name of the member: ")
            new_member = library.add_member(name)
            print(f"Member '{new_member.name}' added successfully with ID {new_member.member_id}.")
        elif choice == "6":
            member_id = int(input("Enter the member ID: "))
            library.search_member_by_id(member_id)
        elif choice == "7":
            member_id = int(input("Enter the member ID: "))
            book_id = int(input("Enter the book ID to borrow: "))
            library.borrow_book(member_id, book_id)
        elif choice == "8":
            member_id = int(input("Enter the member ID: "))
            book_id = int(input("Enter the book ID to return: "))
            library.return_book(member_id, book_id)
        elif choice == "9":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
