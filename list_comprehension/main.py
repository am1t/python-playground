with open("file1.txt") as file:
    list1 = [int(number) for number in file.readlines()]

with open("file2.txt") as file:
    list2 = [int(number) for number in file.readlines()]

result = [number for number in list1 if number in list2]
print(result)