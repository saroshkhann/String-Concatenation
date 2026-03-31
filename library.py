class Library:
    def __init__(self):
        self.book_data = []

    def menu(self):
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search by Author")
        print("6. Exit")

    def add_book(self):
        title = input("Enter the title of book")
        author = input("Enter Author Name")
        copies = int(input("Total Copies"))
        borrowed = 0

        self.book_data.append({"title": title, "author": author, "copies": copies, "borrowed": borrowed})
        print("Book added Successfully")

    def view_book(self):
        counter = 1
        for book in self.book_data:
            print(f"{counter}. {book['title']} - {book['author']} - Available: {book['copies']}")
            counter+=1


    def borrow_book(self):
        book_title = input("Enter book title to borrow: ")
        found = False
        for book in self.book_data:
            if book["title"].lower() == book_title.lower():
                found = True
                if book["copies"] - book["borrowed"] > 0:
                    print("Book borrowed successfuly")
                    book["borrowed"] +=1
                    print(f"Available copies: {book['copies'] - book['borrowed']}")
                else:
                    print("No copies Available")
                break

            if not found:
                print("Book not found!")

    def return_book(self):
        return_book = input("Enter book title to return: ")
        found = False
        for r_book in self.book_data:
            if r_book["title"] == return_book:
                if r_book["borrowed"] > 0:
                    print("Book returned successfully!")
                    r_book["borrowed"] -= 1
                    print(f"Available Copies: {r_book['copies'] - r_book['borrowed']}")
                else:
                    print("No Copies were Borrowed")
                found= True

        if not found:
            print("Book not found!")

    def search_book(self):
        author_name = input("Enter Author Name: ")
        found = False

        for book_author in self.book_data:
            if book_author["author"] == author_name:
                print(f"{book_author['title']} - Available: {book_author['copies'] - book_author['borrowed']}")
                found = True
        if not found:
            print("No books found by this author!")




user_1 = Library()

is_on = True

while is_on:
    user_1.menu()
    choice = int(input("Enter the operation you want to perform: "))

    if choice == 1:
        user_1.add_book()
    elif choice==2:
        user_1.view_book()
    elif choice==3:
        user_1.borrow_book()
    elif choice==4:
        user_1.return_book()
    elif choice==5:
        user_1.search_book()
    elif choice==6:
        print("Exiting program... Goodbye!")
        is_on = False