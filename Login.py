def login():
#Here are the user data
    data = {
    "Name" : "******",
    "Surname" : "******",
    "Age" : "******",
    "Birthday": "******",
    "Adress":"******",
    "Postal Code":"******",
    "Phone Number":"******",
    "City":"******",
    "State": "******",
    }
    #In the db_username and db_passwords put the username and password to unlock the data
    db_username = "******"
    db_password = "******"
    username = input("Enter your username : ")
    password = input("Enter your password : ")
    if username == db_username:
        if password == db_password:
            for s,q in data.items():
                print(s + "  :  "+ q)
        else:
            print("Sorry, your password was incorrect.Try again!")
    else:
        print("""The username that you've entered doesn't belong to an account. Please check your username and try again.""")
login()