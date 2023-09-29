# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = int(input())
BC = int(input())

AC = math.sqrt(AB**2 + BC**2)
H = AC / 2.0
ad = BC / 2

angle = int(round(math.degrees(math.acos(ad/H))))

print(str(angle) + "\u00B0")