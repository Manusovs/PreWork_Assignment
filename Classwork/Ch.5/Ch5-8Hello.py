users = ['admin', 'Dave', 'Scott', 'Paola', 'Tiago']
for user in users:
    if user == "admin":
        print("Hello admin, would you like to see a status report?\n")
    else:
        print("Hello " + user + ", thank you for logging in again. ")
