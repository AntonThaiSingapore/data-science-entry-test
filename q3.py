#q3.py
#Task 1:

def update_dictionary(dct,key,value):
    #check if dct is a dictionary
    if not isinstance(dct,dict):
        return "dct is not a dictionary"

    #check if the key already exists in dct
    if key in dct:
        print("Original value: ",dct[key])

    #update its value
    print("Updated value: ",value)
    dct[key] = value
    return dct

#Task 2:
print("")
print(update_dictionary({},"name", "Alice"))
print("")
print(update_dictionary({"age":25},"age",26))