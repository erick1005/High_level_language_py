import math

# A lambda function is a small anonymous function in Python. It can take any number 
#of arguments but can only have one expression
numbers = [1, 2, 3, 4, 5]

sum = lambda a,b : a - b     # lambda takes two arguments
print(sum(5,2))

larger = lambda x, y : x if x > y else y
print("the largest is: ",(larger(8, 4)))

round_off = lambda z : math.ceil(z)
print(round(0.556))

sq_numbers = []
sq = lambda x : x*x
for x in numbers:
    sq_numbers.append(sq(x))
print(sq_numbers)
