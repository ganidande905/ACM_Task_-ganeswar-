n = int(input("Enter the limit for Fibonacci sequence: ").strip())

while n >= 4 * 10 ** 16:
    print("Enter a number less than 4*10^16")
    n = int(input("Enter the limit for Fibonacci sequence: ").strip())
prev_term = 1
curr_term = 2
even_sum = 0
while curr_term <= n:
    if curr_term % 2 == 0:
        even_sum += curr_term
    prev_term, curr_term = curr_term, prev_term + curr_term

print("Sum of even-valued terms in the Fibonacci sequence up to", n, "is:", even_sum)
