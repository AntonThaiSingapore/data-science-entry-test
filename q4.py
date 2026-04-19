#q4
#Task 1:

def string_reverse(s):
    #check if s is a string
    if not isinstance(s,str):
        return "S must be a string"

    #build a new string in reverse order
    new_str = ""
    for chr in s:
        new_str = chr + new_str

    #return the reversed string
    return new_str

#Task 2:
print(string_reverse("Hello World"))
print(string_reverse("Python"))