fav_places = {"david":["Friendswood","Heaven", "Costa Rica"],
              "marie":["Paris"],
              "carie":["School", "home", "Heaven"]}

for person, place in fav_places.items(): 
    if len(place) == 1:
        print(person.title() + "'s favorite place in the whole world is:")
        print("\t" + place[0])
    else:
        print(person.title() + "'s favorite places are:")
        for single in place:
            print ("\t" + single)
    