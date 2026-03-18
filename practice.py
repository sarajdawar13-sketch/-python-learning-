number=int(input("Entere your number: "))
if number%2 ==0:
    print("Even")
else:
    print("Odd")



number1=int(input("Entere your number: "))      
number2=int(input("Entere your number: "))

if number1>number2:
   print(number1)
else:
    print(number2)



number1=int(input("Entere your number: "))   

if number1 > 0:
    print("Positive")
elif number1 < 0:
    print("Negative") 
else:
    print("zero")


username=str(input("Enter your username: "))
password=int(input("Enter your password: ")) 


if username == "admin":
    if password == 1234:
        print("Login Successfull")
    else:
        print("Login Unsuccessfull")    
else:
    print("Login Unsuccesssfull")



age=int(input("Enter your age: "))
income=int(input("Enter your income:"))

if age>=21 and income>= 30000:
    print("Loan Approoved")
else:
    print("Loan Rejected")
