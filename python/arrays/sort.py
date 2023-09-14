#arr = [1,2,4,5,6,8,3,6,6]

#arr.sort() #sorts array in ascending order
#arr2 = set(arr)   #removes any duplicates in the array
#print(arr2)

if __name__ == '__main__':
    nested_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name, score])

    # sort the nested list by grade
    nested_list.sort(key=lambda x: x[1])

    # find the second lowest grade
    second_lowest_grade = sorted(list(set([x[1] for x in nested_list])))[1]

    # print the names of any student(s) having the second lowest grade
    for name, grade in sorted(nested_list):
        if grade == second_lowest_grade:
            print(name)    