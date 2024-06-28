# we are making a bank project. lets start off by asking the user to create an accounts

# we create an list that stores the accounts info
accounts = []

# making a function which takes the info that the user enters and puts it in the accounts list
def bank_accounts(name,balance):
    user_accounts = {"name": name, "balance": balance}
    accounts.append(user_accounts)
    print("Success")
    print("Your name:", name)
    print("Balance", balance)

# after that we are making a transaction function which makes the user find the name that they want to send a transaction and send it to that accounts
def bank_transaction(name,ammount):
    # we do this by creating a for loop
    for account in accounts:
        if account["name"] == name:
            account["balance"] += ammount

            print("Success")
            print("There balance is now", account["balance"])
        # for some functions we make an else which outputs a message saying the user wasnt found if the user enters the name that is not in the data
        else:
            print("Name not found")

# this is a accounts update function which updates the name for the user
def bank_accounts_update(name,new_name):
    for account in accounts:
        # in the for loop we get 2 arguements name and new_name. name is the current name for the user and new_name is the name that it is updated to. in this line we have a code that checks if the user entered the same name as the current name and if not it updates it
        if account["name"] == name:
            account["name"] = new_name
            
            print("Success")
        else:
            print("Name not found")


# this is a function which deletes the users accounts
def bank_accounts_delete(name):
    # we do this by yet again making a for loop
    for account in accounts:
        # getting the name arguement and removing it from the list "accounts"
        if account["name"] == name:
            accounts.remove(account)
        else:
            print("Name not found")

# this is a function which searches accountss in the data
def bank_accounts_search(name):
    # make a for loop for every accounts
    for account in accounts:
        # if the user enters a name that is in the data it brings out their balance
        if account["name"] == name:
            print("Name:",  account["name"],  "Balance:", account["balance"])
        else:
            print("Nmae not found")

# this is a function which lists all accountss in the data
def bank_accounts_list():
    # we get a for loop to output every accounts it finds
    for account in accounts:
        # and then brings out their balance
        print("Name:", account["name"], "Balance:", account["balance"])
    
# this is the main code that shows up for the user
while True:
    # here we have option to pick
    print("Welcome to JALA BANK")
    print("1. Create accounts")
    print("2. Perform Transaction")
    print("3. Update accounts Info")
    print("4. Delete accounts")
    print("5. Search accounts List")
    print("6. View Customer's List")
    print("7. Exit System")

    # we ask user to pick
    user_choice = input("What would you like? ")

    # if the user picks a number from 1-7. it performs the functions above. for example bank_account function is "1" and so on
    if user_choice == "1":
        name = input("Enter your name: ")
        balance = float(input("Enter your EXACT balance: "))
        bank_accounts(name,balance)

    elif user_choice == "2":
        name = input("Enter their name: ")
        ammount = float(input("How much would you like to send? "))
        bank_transaction(name,ammount)

    elif user_choice == "3":
        name = input("Enter name: ")
        new_name = input("Enter new name: ")
        bank_accounts_update(name,new_name)

    elif user_choice == "4":
        name = input("Enter name: ")
        bank_accounts_delete(name)

    elif user_choice == "5":
        name = input("Enter name: ")
        bank_accounts_search(name)

    elif user_choice == "6":
        bank_accounts_list()
    

    # this will stop the code once the user enters 7
    elif user_choice == "7":
        print("Goodbye")
        break
    
    # if the user enter a number that isnt in the range of 1-7. the program tells them that it is incorrect
    else:
        print("Choice not found. try from 1-7")

