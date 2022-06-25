#6. Largest number 

'''Given a list of numbers, the task is to write a Python program to find the largest number in the given list.

Input : list1 = [10, 20, 4]
Output : 20

Input : list2 = [20, 10, 20, 4, 100]
Output : 100'''

list = [-10, -20, -50,-40, 30]
max=list[0]
# max=0
for number in list:
    if number> max:
        max=number
print(max)