n = int(input("Enter the size of array: "))
while n <= 0:
    print("Size of the array should be greater than 0.")
    n = int(input("Enter the size of array: "))
    
p = list(map(int, input("Enter space generated integers: ").split()))

for k in p:
    while k >= 1000:
        print("Array elements should be less than or equal to 1000.")
        p = list(map(int, input("Enter space generated integers: ").split()))

array_sum = sum(p)
print("Sum of elements:", array_sum)      

