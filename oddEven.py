evenCount = 0
oddCount = 0
count = int(input("How many numbers : "))
for i in range(count):
    print("Enter number",i+1,end=": ")
    num = int(input())
    if num % 2 == 0 :
        evenCount = evenCount+1
    else:
        oddCount = oddCount+1
print("Odd count: ",oddCount,"\nEven Count: ",evenCount)

"""
output
.......
How many numbers : 5
Enter number 1: 2
Enter number 2: 3
Enter number 3: 3
Enter number 4: 8
Enter number 5: 4
Odd count:  2 
Even Count:  3

"""
