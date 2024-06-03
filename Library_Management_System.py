from datetime import date

books_inventory = {'harry potter and the goblet of fire':
{'capitalized title' : 'Harry Potter and the Goblet of Fire',
'author' : 'J.K. Rowling',
'genre' : 'fiction',
'recommended_age' : 'teenager',
'copies' : 5,
'current_borrowers' :[],
'dates_borrowed' : []},
'the borrowers' :
{'capitalized title' : 'The Borrowers',
'author' : 'Mary Norton',
'genre' : 'fiction',
'recommended_age' : 'older child',
'copies' : 3,
'current_borrowers' : [],
'dates_borrowed' : []}}

users_info = {'user1' : {'borrowed_books' : [], 'dates_borrowed' : [], 'fines' : 0},
              'user2' : {'borrowed_books' : [], 'dates_borrowed' : [], 'fines' : 0}}

# set the maximum number of days that a book can be borrowed for
max_days = 14

# set the maximum number of books that a user can borrow at one time
max_books = 5

# set the daily fee for late book return (in £)
daily_fee = int(0.3)

# create function to add books to books_inventory

# create function to add users to users_info

# create function asking the user for the book title and checking it exists
def book_title_check(books_inventory):
    while True:
        book_title = input("Please enter the title of the book: ").lower()
        book_title = book_title.strip()
        if book_title in books_inventory:
            break
        else:
            print("Error - this book title wasn't recognised.")
    return book_title


# create function asking user for the username and checking it exists
def username_check(users_info):
    while True:
        username = input("Please enter the username of the customer: ").lower()
        username = username.strip()
        username = username.replace(" ", "")
        if username in users_info:
            break
        else:
            print("Error - this username was not recognised")
    return username

# create function to check out books
def checkout_book(books_inventory, users_info, today):
    # ask user to input book title by calling the book_title_check function
    book_title = book_title_check(books_inventory)
    # ask user to input the username by calling the username_check function
    username = username_check(users_info)
    # if there are spare copies to lend and the user hasn't exceeded their allowance, add the book and date to users_info and add the user and date to the books_inventory
    if books_inventory[book_title]['copies'] > 0 and len(users_info[username]['borrowed_books']) < max_books:
        books_inventory[book_title]['current_borrowers'].append(username)
        books_inventory[book_title]['dates_borrowed'].append(today)
        books_inventory[book_title]['copies'] -= 1
        users_info[username]['borrowed_books'].append(book_title)
        users_info[username]['dates_borrowed'].append(today)
        print(f"{book_title} checked out successfully to {username}")
    elif books_inventory[book_title]['copies'] == 0:
        print(f"There are no copies of this book available.")
    else:
        print(f"This user has reached the maximum book allowance and cannot borrow anymore books.")
    print(f"""
You have successfully checked out {books_inventory[book_title]['capitalized title']} to {username.capitalize()}
""")
    return books_inventory, users_info

# create function to return books
def return_book(books_inventory, users_info, today, daily_fee):
    # ask user to input book title by calling the book_title_check function
    book_title = book_title_check(books_inventory)
    # ask user to input the username by calling the username_check function
    username = username_check(users_info)
    # find book in users_info and pull out the corresponding date
    for index in range(len(users_info[username]['borrowed_books'])):
        if users_info[username]['borrowed_books'][index] == book_title:
            checkout_date = users_info[username]['dates_borrowed'][index]
    date_difference = abs(today - checkout_date).days
    if date_difference > max_days:
        users_info[username]['fines'] +=1
        fine = daily_fee * date_difference
        print(f"""
You are returning the book after the return date.
You must pay a fine of £{fine:2f}.
""")
    books_inventory[book_title]['copies'] += 1
    for index in range(len(books_inventory[book_title]['current_borrowers'])):
        if books_inventory[book_title]['current_borrowers'][index] == username:
            books_inventory[book_title]['current_borrowers'].pop(index)
            books_inventory[book_title]['dates_borrowed'].pop(index)
    for index in range(len(users_info[username]['borrowed_books'])):
            users_info[username][borrowed_books]

# create function that creates list of users with overdue books

# create function displaying book info

# create function displaying user info

# create reward system for members who have a good track record of returning books on time.

# create the variable for today's date
today = date.today()

# print menu, showing the user their options
print(f"""
Welcome to the Library Management System.
Today's date is {today}.

You can perform the following functions:
1 - Checkout a book
2 - Return a book
3 - User management (see info, add user, delete user)
4 - Book management (see info, add book, delete book)
5 - Show list of users with overdue books
6 - Show list of members with a good track record of returning books on time
""")

# ask user which menu option they would like to select
while True:
  try:
    menu_select = int(input("Enter the menu option you would like to select: "))
  except ValueError:
                      print("Error - you must enter a number.")
  except exception as e:
                      print(f"{e}")
  else:
      break

# if the user selects 1 (checkout a book), run the relevant function, inputting the books_inventory, users_info dictionaries and today's date. Return the updated dictionaries.
if menu_select == 1:
    checkout_book_function = checkout_book(books_inventory, users_info, today)
    books_inventory = checkout_book_function[0]
    users_info = checkout_book_function[1]
    print(books_inventory)
    print(users_info)

#if menu_select == 2