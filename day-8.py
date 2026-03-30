count = 1

while count <= 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1


while True:
    num=int(input("Enter a no(0 to stop): "))

    if num==0:
        break

    print("you enterted ",num)



#PROBLEM 1

count=1
while count<= 10:
    print(count)
    count +=1


#Problem2
n=int(input("Enter your no : "))

total = n * (n+1)//2
print(total)

