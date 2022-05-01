#this program is used to divide username and domain
def email_slicer():
    email= input("Enter your email: ").strip()
    #this line take everthing before '@'
    user_name = email[:email.index("@")]
    #by default is going to return '@example.com'
    domain_name = email[email.index("@"):]   # +1 can be added to prevent taking '@'
    user_view= "your username is {} & your domain name is {}".format(user_name,domain_name)
    return user_view
print(email_slicer())


