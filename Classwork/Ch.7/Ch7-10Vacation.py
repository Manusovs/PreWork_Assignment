Vacation = []
flag = True

while flag == True:  
    Vacation.append(input("Where would you go for your dream vacation?  "))
    repeat = input("is there another person to fill out the poll? (yes/no)  ")
    if repeat == "no":
        flag = False
print ("\n\nThe following places were listed for dream vacations:")
for polls in Vacation:
    print(polls)
