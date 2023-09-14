# a map function takes in a lambda fxn and an iterable
# it returns an object adress so it should always be casted into what is required e.g a list

numbers = [1, 2, 3, 4, 5]

squares = map(lambda x : x * x, numbers)
print(list(squares))

num1 = [6, 7, 8, 9]
num2 = [4, 3, 2, 1]

sum_results = map(lambda n1, n2 : n1 + n2, num1, num2)
print(list(sum_results))