'''
WAP that allows a liberarian to add several books to a library.For each book, ask the user to enter its title and the number of copies.Stores each book and its avaliable copy count in a dictionary.
After the books have been added, display a menu that lets the user issue a book, return a book, display all books, or exit the program.
Apply these conditions:
-book titles should be compared without distinguished uppercase and lowercase letters.
-A book can be issued only if it exist in the library and at least 1 copy is available.
-Issuing a book decreases its available copy count by one.
-A book can be returned only if it exists in the library and at least one copy has already been issued.
-Returning a book increases its available copy count by one.
-Display an appropriate message for an unavailable book, an invalid choice, or an invalid no. of copies. 
'''
class Library:
    def __init__(self):
        self.books = {}

    def add_books(self,title,copies):
        key = title.lower()
        self.books[key] = [title,copies,copies]

    def issue_book(self,title):
        key = title.lower()
        if key not in self.books:
            print("Book not found.")
        elif self.books[key][1]==0:
            print("No copies are available")
        else:
            self.books[key][1] -= 1
            print("Book issued successfully")

    def return_book(self, title):
        key = title.lower()
        if key not in self.books:
            print("Book not found.")
        elif self.books[key][1]==self.books[key][0]:
            print("No copies  of books are currently  available")
        else:
            self.books[key][1] += 1
            print("Book returned successfully")

    def display(self):
        print("\nLibrary books: ")
        for details in self.books.values():
            title = details[0]
            available_copies = details[1]
            print(title, "Available copies:", available_copies)


lib = Library()
no_of_books = int(input("How many different books do u want to add? "))

for i in range(no_of_books):
    title = input("Enter title: ").strip()
    copies = int(input("Enter num of copies: "))
    if copies<=0:
        print("Number of copies must be greater than zero. ")
    else:
        lib.add_books(title,copies)
        print("Book add successfully.")
while True:
    print("\n1. Issue Book\n2. Return Book")
    print("3. Display Books\n4. Exit")
    ch = input("Enter choice: ")

    if ch == '1':
        title = input("Enter title of issued book: ").strip()
        lib.issue_book(title)
    elif ch == '2':
        title = input("Enter title of returned book: ").strip()
        lib.return_book(title)
    elif ch == '3':
        lib.display()
    elif ch == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice")
