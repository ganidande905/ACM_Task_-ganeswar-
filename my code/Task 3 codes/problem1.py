k = int(input("Number Of Parameters: "))
if -100 <= k <= 100:
    l = [int(i) for i in input("parameters: ").split()]
    sum_of_input = sum(i for i in l if i % 2 == 1)
    print(sum_of_input)
else:
    print("k is out of the valid range")
