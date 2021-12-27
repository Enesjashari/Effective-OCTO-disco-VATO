import functools as ft
#The login into this sowftware,it also can be ingored
database_username = "*****"
database_password = "*****"

username = input("Enter your username : ")
password = input("Enter your password : ")

while True:
    if database_username != username and database_password != password:
        continue
    else:
        break

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

#If there is no x product it will not calculate it.This is required to use,it mustn't get commented.
Number_of_Product_filter = filter(lambda s :s["Number_of_Product"]>0,Products)

#You can use this only if you want to Discount all the product by same percent,else just make it comment.
#BE CAREFUL! To use this you need to make all Discount values =0 ,but it isn't necessary.
DISCOUNT = 0
kml = []
for s in Products:
    s["Discount"] += DISCOUNT
    kml.append(s)
#This is used to calculate products that custumer purchased.
l =lambda s,q:s + ((q["Number_of_Product"] * q["Product_price"]) - (q["Product_price"] * q["Discount"]/100))


final = ft.reduce(l,Number_of_Product_filter,0)
print("Total"+ " "+ str(final) + " " + "euro!")#dollar,paund etc.