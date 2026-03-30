def square(num):
    return num*num
result=square(4)
print("Square is ",result)

#PROBLEM 1
def add(a,b):
    return a+b
result=add(5,4)
print(result)

#PROBLEM 2
def area_of_a_cirlce(r):
    return 3.14 *r*r 
radius=float(input("Enter radius: "))
area= area_of_a_cirlce(radius)
print(f"Area of a cirle is {area}")    
 
#PROBLEM3
def SI(p,r,t):
    return(p*r*t)/100
p=int(input("enter principal:"))
r=int(input("enter rate of interest: "))
t=int(input("enter time: "))
result=SI(p,r,t)
print(f"Simple interst is {result}")

#problem
def student_marks(m1, m2, m3):
    total = m1 + m2 + m3
    avg = total / 3
    return total, avg

total, avg = student_marks(80, 90, 85)

print("Total:", total)
print("Average:", avg)