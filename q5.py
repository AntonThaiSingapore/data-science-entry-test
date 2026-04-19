#q5
#Task 1:

def check_divisibility(num,divisor):
    #check if both num and divisor are numbers
    if not(isinstance(num, (int, float))) or not(isinstance(divisor, (int, float))):
        return "These are not numbers"

    #check if divisor is zeo
    if divisor == 0:
        return "You can't divide by zero"

    #return True if num is divisible by divisor, False otherwise
    return num % divisor == 0


#Task 2:
print(check_divisibility(10,2))
print(check_divisibility(7,3))