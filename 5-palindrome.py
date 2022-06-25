#5.Palindrome

'''Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.
Input : malayalam
Output : Yes

Input : geeks
Output : No'''

text=input('word: ')

rev=''.join(reversed(text))
if text == rev:
    print('yes')
else:
    print('no')