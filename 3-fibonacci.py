#3. Fibonacci

'''Write a Fibonacci sequence using python. A Fibonacci sequence is an infinite series of numbers that are created by adding the last two numbers in the series. A series would start with the numbers 1 and 1 in place, followed by 1 (0+1). 2(1+1), 3(1+2), 5(3+2), etc.. 

0 1 1 2 3 5 8 13 21 ....'''

def fibo(n):
    if n<=1:
        return n
    else: 
        return (fibo(n-1)+fibo(n-2))
nterms=int(input('please enter a number: '))
if nterms <= 0:
    print("Please enter a positive number")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(fibo(i))