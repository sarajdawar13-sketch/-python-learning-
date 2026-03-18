#EXAMPLE-1
age=int(input('Enter your age: '))
if age>= 18:
    print('you can vote')
else:
    print('you cannot vote')

#EXAMPLE-2  
marks=int(input('Enter your marks: '))
          
if marks>= 90:
    print("Grade A")
elif marks>= 75:
    print("Grade B")
elif marks>= 60:
    print("Grade C")
else:
    print("Fail")          


#EXAMPLE-3
age=int(input("Enter your age : "))
citizen=input('Are you citizen (yes/no): ')

if age>= 18:
    if citizen=="yes":
        print("you can vote")
    else:
        print(" Not a citizen") 
else:
    print("you are underage")


