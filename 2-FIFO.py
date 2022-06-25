#2.FIFO

'''A first-in-first-out (FIFO) structure, also called a “queue,” is a list that gets new elements added at the end, while elements from the front are removed and processed. Write a program that processes a queue. In a loop, ask the user for input. If the user just presses the Enter key, the program ends. If the user enters anything else, except for a single question mark (?), the program considers what the user entered a new element and appends it to the queue. If the user enters a single question mark, the program pops the first element from the queue and displays it. You have to take into account that the user might type a question mark even if the queue is empty.'''

list=[]
def fifo ():
    text=input('enter somthing: ')
    if text =='':
        print(list)
    elif text=='?' and len(list)>0:
        print(list.pop(0))
        fifo()
    elif text=='?' and len(list)==0:
        fifo()
    else:
        list.append(text)
        fifo()

fifo()