# Create a program that asks the user for their top 3 fav boos, stores them in a list, and prints the list in a sorted order.

my_books = []

first_book = input("Enter your first favorite book: ")
second_book = input("Enter your second favorite book: ")
third_book = input("Enter your third favorite book: ")

my_books.append(first_book)
my_books.append(second_book)
my_books.append(third_book)

my_books.sort()

print(my_books)
