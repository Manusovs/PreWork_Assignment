toppings = input("Please enter a pizza topping.\nWhen you are done hit quit.  ")

while toppings != "quit":
    if toppings.lower() != "quit":
        print(toppings)
        toppings = input("We will add this to your pizza.\nPlease enter your next topping.\nWhen you are done hit quit.  ")