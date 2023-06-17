current_users = ["Paola", "Scott", "Meng","talia", "Tiago"]
new_users = ["Azizat", "Raul", "An", "Talia", "TIAGO"]

Lowcurr_users= [x.lower() for x in current_users]
for new_user in new_users:
    if new_user.lower() in Lowcurr_users:
        print("Please choose a new username.  This username is taken.")
    else:
        print("Username is available.")


