

def create_sandwich():
    sandwich=[]
    flag = True
    while flag == True:
        sandwichtopping = input("What would you like on your sandwich? \ntype final when there is nothing else to add.  ")
        if sandwichtopping.lower() == "final":
            flag = False    
        else:
            sandwich.append(sandwichtopping)
    print("\nYou have a sandwich with",end = ' ')
    for i in range(len(sandwich)):
        print(sandwich[i] + ",", end = ' ' )
    print ("\n")
    
    



# while flag == True:
#     sandwichtopping = input("What would you like on your sandwich? \ntype final when there is nothing else to add.  ")
#     if sandwichtopping.lower() == "final":
#         flag = False    
#     else:
#         sandwich.append(sandwichtopping)
# print("You have a sandwich with ",end = ' ')

create_sandwich()
create_sandwich()
create_sandwich()