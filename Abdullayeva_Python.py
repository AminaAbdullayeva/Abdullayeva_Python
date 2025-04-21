#Task 1
number= int(input())
if number > 7:
    print("Hello")

#task 2
name= input("input a name: ")
if name=="John":
    print("Hello, John")
else:
    print("There is no such name")

#task3
print([num for num in map(int, input("Enter numbers separated by spaces: ").split()) if num % 3 == 0])
