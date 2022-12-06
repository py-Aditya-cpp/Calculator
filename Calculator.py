print("Hello ," , "I am calculator ," , "How can I help you!!")
print()
print('''Operations :
1. Add
2. Subtract
3. Multiply
4. Divide
5. Percentage
6. Exponent
7. Floor Divide(//)
8. Pi(π)
9. Equal(=)''')
print()
y = 1
a=float(input("Enter first number : "))
while y == 1:
    print()
    Operation=input("Enter operation :  ")
    if Operation =="=":
        print(a)
        break
    print()
    b=float(input("Enter other number :  "))
    print()
    if Operation != "9" :
        if Operation== '+' :
            c = a+b
            print(a , "+" , b , "=" , c, "_")
            print()
        elif Operation== '-' :
            c = a-b
            print(a , "-" , b , '=' , c, "_")
            print()
        elif Operation== '*' :
            c = a*b
            print(a , "*" , b , '=' , c, "_")
            print()
        elif Operation== '/' :
            c = a/b
            print(a , "/" , b , '=' , c, "_")
            print()
        elif Operation== '%' :
            c = (a/b)*100
            print(a , "%" , "of" , b , '=' , c, "_")
            print()
        elif Operation== '**' :
            c = a**b
            print(a , "^" , b , '=' , c, "_")
            print()
        elif Operation == '//' :
            c = a//b
            print(a , "//", b , "=" , c, "_")
            print()
        elif Operation == 'pi' :
            import math
            c = math.pi
            d = a*b*c
            print(a, "π", b, "=", d, "_")
        elif Operation == '=' :
            print(a)
        else:
            print("Invalid Input")
            print()
        a = c
    else :
        break
print()
print("Thanks for using this calculator!!")
