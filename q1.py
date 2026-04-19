#q1.py
#Task 1:

def swap(x,y):
    #check if x and y are numbers
    if not(isinstance(x,(int,float)) and isinstance (y,(int,float))):
        return -1
    #swap x and y
    x,y = y,x
    print("x value now is: ",x)
    print("y value now is: ",y)
    return ""

#Task 2:
print(swap("Apple",10))
print(swap(9,17))
