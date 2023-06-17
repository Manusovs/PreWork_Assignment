"""Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing"""
def first_odds():
    """print all the odds numbers and return nothing (not just none)"""
    for i in range(1,101,2):
        print(i)
    return "nothing" #return not needed if you just want none for return instead of actually "nothing"
print(first_odds())   #this is a test to make sure it would both print odds and return nothing
                        #without telling it to specifially print nothing, it actually prints "none"