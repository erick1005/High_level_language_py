from collections import Counter

print("enter number of shoes")
num_shoes =  int(input())

print("enter shoes sizes")
shoe_sizes = Counter(map(int,input().split()))

print("enter number of customers")
num_of_customers = int(input())
earnings = 0

for i in range(num_of_customers):
    size, price = map(int, input().split())
    if shoe_sizes[size]:
        earnings += price
        shoe_sizes -= 1


print(shoe_sizes)
print(earnings)