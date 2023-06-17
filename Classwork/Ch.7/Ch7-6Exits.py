# toppings = input("Please enter a pizza topping.\nWhen you are done hit quit.  ") #iteration 1 uses conditional for the word "quit"

# while toppings != "quit":
#     if toppings.lower() != "quit":
#         print(toppings)
#         toppings = input("We will add this to your pizza.\nPlease enter your next topping.\nWhen you are done hit quit.  ")



# toppings = input("Please enter a pizza topping.\nWhen you are done hit quit.  ") #iteration 2 uses active variable that changes the flag (on the word "quit")
# flag = True

# while flag == True:
#     if toppings.lower() == "quit":
#         flag = False
#     else: 
#         print(toppings)
#         toppings = input("We will add this to your pizza.\nPlease enter your next topping.\nWhen you are done hit quit.  ")

        


toppings = input("Please enter a pizza topping.\nWhen you are done hit quit.  ") #iteration 3 uses a break on the word "quit"


while True:
    if toppings.lower() == "quit":
        break
    else: 
        print(toppings)
        toppings = input("We will add this to your pizza.\nPlease enter your next topping.\nWhen you are done hit quit.  ")