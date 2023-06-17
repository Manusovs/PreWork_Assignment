users = ['admin', 'Dave', 'Scott', 'Paola', 'Tiago']#this is overwritten and is kept for history.  
users = []
if users:
    for user in users:
        if user == "admin":
            print("Hello admin, would you like to see a status report?\n")
        else:
            print("Hello " + user + ", thank you for logging in again. ")
else: 
    print ("We need some users.")
