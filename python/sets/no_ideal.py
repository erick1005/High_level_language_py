try:
    n, m = map(int, input().split())
    set_elements = set(map(int, input().split()))
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))
except ValueError:
    print("Please enter only integers separated by spaces.")
    exit()

set_a_happiness = 0

try:
    for element in set_a:
        if element in set_elements:
            set_a_happiness += 1

    for element in set_b:
        if element in set_elements:
            set_a_happiness -= 1
except TypeError:
    print("An error occurred while processing the sets.")
    
print(set_a_happiness)
