# Program to practice dictionaries. Simulates a library.
# Idea to add: Save library data (books, users) in external document (.csv)
# Idea to add: New users can register


library_list_books = {
    "Lord of the Rings": False,
    "Game of Thrones": False,
    "The Hobbit": False,
    "The Shining": False,
    "Advanced Analytics": False,
    "House of Cards": True,
    "Hunger Games": True,
    "Breakfast at Tiffanies": True,
}
user_list_rentings = {
    123: {"Lord of the Rings": 5,
          "Game of Thrones": 3,
          },
    456: {"The Hobbit": 2,
          "The Shining": 6,
          },
    789: {"Advanced Analytics": 12,
          }
    }


def user_type():
    if user_class == "A":
        admin_console()
    if user_class == "C":
        customer_console()


def admin_console():
    global x
    global y
    x = "admin"
    y = "(S)tatus books, (L)ist of books due, (C)ustomer data"


def customer_console():
    global x
    global y
    x = "customer"
    y = "(C)heck rented books, (R)eturn book, (N)ew rental"


def user_rentals(num):
    rentals = str()
    for i in user_list_rentings[num]:
        rentals += i+" / "
    print("Books currently rented:", rentals)


def customer_choice(choice):
    if choice == "C":
        user_rentals(user_id)
    if choice == "R":
        return_function()
    if choice == "N":
        rental_overview()
        rental_function()


def return_function():
    user_rentals(user_id)
    book = str(input("Which book do you want to return:\t"))
    library_list_books[book] = True
    del user_list_rentings[user_id][book]


def rental_overview():
    for book, status in library_list_books.items():
        if status:
            print("Available:", book)


def rental_function():
    rental = str(input("Which book to rent:\t"))
    library_list_books[rental] = False
    user_list_rentings[user_id][rental] = 0


def admin_choice(choice):
    if choice == "S":
        for i, h in library_list_books.items():
            print(h, "\t", i)
    if choice == "L":
        books_due()
    if choice == "C":
        for user, rentals in user_list_rentings.items():
            for books, days in rentals.items():
                print("Customer:\t", user, "\tCurrently rented:\t", books)


def books_due():
    for key_library, item_user in user_list_rentings.items():
        for key_user, value_user in item_user.items():
            if value_user > 5:
                print("User ID: ", key_library, "\tBooks due: ", key_user)


user_class = str(input("(C)ustomer or (A)dmin: ")).upper()
user_id = int(input("Enter user ID [Test IDs: 123, 456, 789]:"))
user_type()
print(f"\n\nYour are logged in as {x}")
while True:
    print(f"Please select:  {y}")
    choice = str(input("Your choice: ").upper())
    if user_class == "C":
        customer_choice(choice)
    if user_class == "A":
        admin_choice(choice)
