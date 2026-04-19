#q2
#Task 1:

def find_and_replace(lst,find_val,replace_val):
    #check if lst is a list
    if not isinstance(lst,list):
        print("lst is not a list")
        return ""

    #loop thru the list using index i from 0 to the length of lst -1
    for i in range(len(lst)):
        if lst[i] == find_val:
            #replace the find_val
            lst[i] = replace_val

    #return the modified list
    return lst

# Task 2:
print(find_and_replace([1,2,3,4,2,2],2,5))
print(find_and_replace(["apple", "banana", "apple"],"apple", "orange"))