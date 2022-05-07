# This is a simple calculator with four basic function
# User inputs 
functions_wanted = input('Calculator can do these math calculations: \n     plus \n     minus \n    multiply \n     devide \n Choose one:  ').strip()
x = int(input('x: '))
y = int(input('y: '))


def calc(operation):
    def plus(x,y):
        return x +y

    def minus(x,y):
        return x-y

    def multiplication(x,y):
        return x * y

    def devide(x,y):
        return x /y

    if operation == "plus":
        return plus(x,y)
    elif operation =="minus":
        return minus(x,y)
    elif operation =="multiplication":
        return multiplication(x,y)
    elif operation =="devide":
        return devide(x,y)

print(calc(functions_wanted))




