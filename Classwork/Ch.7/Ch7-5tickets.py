age = ""
while age.lower() != "quit": 
    age = input("What is your age? (type QUIT to end program)   ")
    if age.lower() == "quit":
        break
    else:
        age = float(age)
    if age < 3:
        print("Ticket is $0")
    elif age <= 12:
        print("Ticket is $10")
    elif age > 12:
        print("Ticket is $15")
    age = str(age)
    
