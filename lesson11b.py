# create a class Book, with the following:
# states: author, title, price, quantity
# methods : show_book(), change_price()
# Get two instances of the class Book:

class Book:
    def __init__(self,author,title,price,quantity) :
        
        self.author = author
        self.title = title
        self.price = price
        self.quantity = quantity

    def show_book(self):
        print(f"The author of {self.title} is {self.author} ")
        print(f"The price is $ {self.price} and we have {self.quantity} copies ")

    def change_price(self):
        new_price = self.price -100.01
        print(f"The price of the book is now from $ {self.price} to $ {new_price} dicounted price. Save 20% OFF ")

book1 = Book("J.K.ROWLING",
             "Harry Potter And The Sourcere's Stone",
             300,
             45)
book1.show_book()
book1.change_price()

book2 = Book(
    input("Enter the Author: "),
    input("Ente the Book: "),
    int(input("Enter the Price: ")),
    int(input("Enter the Number of Copies: "))
)