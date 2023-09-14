# Enter your code here. Read input from STDIN. Print output to STDOUT

M = int(input())
set_a = set(map(int, input().split()))
N = int(input())
set_b = set(map(int, input().split()))

data_a = set_a.difference(set_b)
data_b = set_b.difference(set_a)

data = sorted(data_a.union(data_b))

#data_a = sorted(list(set_a.difference(set_b)))
#data_b = sorted(list(set_b.difference(set_a)))

#print(data_a)
#print(data_b)


for element in data:
    print(element)
