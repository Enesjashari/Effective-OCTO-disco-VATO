import functools as ft

#You can delete some line of Products and you also can add line just copy & paste.
Products = [
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},  
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},  
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},  
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},  
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},  
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},  
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},  
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},  
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},  
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},  
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    {"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},
    ]
#{"Name_of_product":"*****","Number_of_Product":0,"Product_price":0,"Discount":0},  

#If there is 0 Number_of_Product it will not conside as a parameter and calculate it.This is required to use,it mustn't get commented.
Number_of_Product_filter = filter(lambda s :s["Number_of_Product"]>0,Products)

#You can use this only if you want to Discount all the product by same percent,else just make it comment.
#BE CAREFUL! To use this you need to make all Discount values =0 ,but it isn't necessary.
DISCOUNT = 0
kml = []
for s in Products:
    s["Discount"] += DISCOUNT
    kml.append(s)
#This is The Logic Brain,used to calculate products that custumer purchased,It also conside other parameters as well.
l =lambda s,q:s + ((q["Number_of_Product"] * q["Product_price"]) - (q["Product_price"] * q["Discount"]/100))
final = ft.reduce(l,Number_of_Product_filter,0)

#The Sign in can be ignored or deleted as well.
#More users can be added.
Users = {
"Robert" : "BronxBOY",
"Bill" : "Billy666",
"Darlene":"0124421334"
    }
#The Advanced Sign in with Database Users.
username = input("Enter your username : ")
password = input("Enter your password : ")
for s,q in Users.items():
    if username == s and password == q:
        print("Total"+ " "+ str(final) + " " + "euro!") #The current CURRENCIE is changeble>You can convert it into Dollar,Paund etc.
    elif username == s or password == q:
        print("Sorry,Your username/password is wrong.Try again.")









