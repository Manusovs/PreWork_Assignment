"""Write a function to check to see if all numbers in list are consecutive numbers. 
For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
The return should be boolean Type."""

# test_list=[4,5,6,7,8,] #this is a test list to test the function

def is_consecutive(a_list):
    """This determines if numbers are consecutive"""
    order = True
    for i in range(len(a_list)-1): # I used 1 less than the numbers of items in the list to iterate
        if a_list[i] != a_list[i+1]-1: #I then used my iteration to mark the position in the list
            order = False
    return order
    
#print(is_consecutive(test_list)) # this is a test to test the function
    