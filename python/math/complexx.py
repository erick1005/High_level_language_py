import cmath

complex_num = complex(input())

#the value or r sqrt of x2 + y2
#z = x + yj
r = abs(complex_num)

#the value of u
u = cmath.phase(complex_num)

print(r)
print(u)
