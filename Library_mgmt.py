"""2. Create a Library Management System using Class and Object in Python.
What to Do
1. Create a class named Book.
2. Create a constructor __init__() to initialize:
o Book name
o Book ID
o Author name
o Availability status
3. Create a display_book() method to display book details.
4. Create a issue_book() method:
o Check whether the book is available. 
o If available, issue the book and change its status.
o If already issued, display an appropriate message.
5. Create a return_book() method:
o Return the issued book.
o Change its availability status back to available.
6. Create a check_availability() method to display whether the book is available or
issued."""



class Book:
    def __init__(self, book_name, book_id, author_name):
        self.book_name = book_name
        self.book_id = book_id
        self.author_name = author_name
        self.availabile = True

    def display_book(self):
        print("Book name: ", self.book_name)
        print("Book id: ", self.book_id)
        print("Book Author: ", self.author_name)
        if self.availabile:
            print("Status :  Available")
        else:
            print("Status : Issued")

    def issue_book(self):
        if self.availabile:
            self.availabile = False
            print("Issue the book")
        else:
            print("Book is already issue")

    def return_book(self):
        if not self.availabile:
            self.availabile = True
            print("Book return successfully")
        else:
            print("Book is already in the library")

    def check_availability(self):
        if self.availabile:
            print("Book is available")
        else:
            print("Book is issue")

book_name = input("Enter Book name: ")
book_id = int(input("Enter book id: "))
author_name = input("Enter author name: ")


obj = Book(book_name, book_id, author_name)

while True:
    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            obj.display_book()

        case 2:
            obj.issue_book()

        case 3:
            obj.check_availability()

        case 4:
            print("Thank you")

