#4.Counting Letters

'''Write a program that counts the Number of Characters Occurring in a String. 


print(counting_number("an","banan")) # 2

After that replace the duplicated characters with an empty string.

'''

   
def counting_number(x,y):
    return('the number is : {}, new word: {}'.format(y.count(x), y.replace(x, '')))
print(counting_number("mus","mustafa"))