#Class that defines what a book is and its properties.
class Book:
    def __init__(self, title, isbn, publisher, price, course):
        self.title = title
        self.isbn = isbn
        self.publisher = publisher
        self.price = price
        self.course = course
#Class that takes in 
class Bookstore:
    def __init__(self, books):
        self.books = books

#Using an array we created a selection / list of books.
#Nvm, Python doesn't have arrays they only have lists. Which then means we can add to the books below.
books = [
    Book("The Great Gatsby", 978-3-16-148410-0, "F. Scott Fitzgerald", 12.99, "English 101"),
    Book("To Kill a Mockingbird", 978-0-306-40615-7, "Harper Lee", 9.99, "English 201"),
    Book("1984", 978-1-86197-876-9, "George Orwell", 8.99, "AP English"),
]

#Function that displays all books once called apon.
def DisplayAllBooks():
    for Book in books:
        print(Book.title, Book.isbn, Book.publisher, Book.price, Book.course)    

#Function that allows the user to search for a book by title or isbn.
def SearchBook():
    #Using input, won't this give me an error for isbn since it returns a string and not a number?
    searchResult = input("What book are you looking for? (title or isbn)")
    for Book in books:
        #Checking to see if the result does not match a title or a isbn, printing out an error and returning.
        if searchResult != Book.title and searchResult != Book.isbn:
            print("Book not found")
            return
        #I think I could just use an else since I error checked above, but I did this anyways.
        elseif: searchResult == Book.title or searchResult == Book.isbn
        print(Book.title, Book.isbn, Book.publisher, Book.price, Book.course)

#Function to add/create a new book.
def AddBook():
    print("What book would you like to add? (have the necessary information ready)")
    booktitle = input("What is your books title?")
    bookisbn = input("What is your books isbn?")
    bookpublisher = input("What is your books publisher?")
    bookprice = input("What is your books price?")
    bookcourse = input("What is your books course?")

#Creating a new book with the information the user inputted.
    newbook = Book(booktitle, bookisbn, bookpublisher, bookprice, bookcourse)

#Adding the new book to the list of books.
    books.append(newbook)

#Function to remove a book from the list.
    def RemoveBook():
        bookisbn = input("What is the books isbn number you would like to remove?")
        for Book in books:
            #If the isbn does not match, print and return out. 
            if bookisbn != Book.isbn:
                print("Book not found")
                return
            #Since we found a book if we get this far, remove it, print, and return.
            else:
                books.remove(Book)
                print("Book removed")
                return

#Calculating the total price of someones order.
    def CalculateTotalPrice():
        totalprice = 0

        #Using a while loop to keep asking the user for books until they are done.
        while True:
            bookisbn = input("What is the books isbn number you would like to add to your order? (type done when finished)")
            #If the user types done, break out of the loop and print the total price.
            if bookisbn == "done":
                break
            #If the user types anything else, check to see if it matches a book.
            else:
                for Book in books:
                    #If it does not match, print and return.
                    if bookisbn != Book.isbn:
                        print("Book not found")
                        return
                    #If it does match, add the price to the total price.
                    else:
                        totalprice += Book.price
                        #Printing out the total price once done using the function.
                        print("Your total price is " + totalprice)