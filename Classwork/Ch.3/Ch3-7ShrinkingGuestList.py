dead = ["Ghandi", "David", "Einstein"]
print(dead[0] + ', you are cordially invited to dinner from the afterlife to the "not dead life"')
print(dead[1] + ', you are cordially invited to dinner from the afterlife to the "not dead life"')
print(dead[-1] + ', you are cordially invited to dinner from the afterlife to the "not dead life"\n')#added an extra line, to separate the different sections
pdead= dead.pop(0)
print(pdead + ", I'm sorry you weren't able to make it \n")# added an extra line to separate the different sections
dead.append("Kadie")
print(dead[0] + ', you are cordially invited to dinner from the afterlife to the "not dead life"')
print(dead[1] + ', you are cordially invited to dinner from the afterlife to the "not dead life"')
print(dead[-1] + ', you are cordially invited to dinner from the afterlife to the "not dead life"\n')
print("Everyone, good news we found a bigger dinner table!\n")
dead.insert(0, "Alexander the Great")
dead.insert(2, "Marie Curie")
dead.append("John Paul")
print(dead)
print(dead[0] + ', you are cordially invited to dinner from the afterlife to the "not dead life"')
print(dead[1] + ', you are cordially invited to dinner from the afterlife to the "not dead life"')
print(dead[2] + ', you are cordially invited to dinner from the afterlife to the "not dead life"')
print(dead[3] + ', you are cordially invited to dinner from the afterlife to the "not dead life"')
print(dead[4] + ', you are cordially invited to dinner from the afterlife to the "not dead life"')
print(dead[-1] + ', you are cordially invited to dinner from the afterlife to the "not dead life"\n')
print("Sorry, everyone the table won't arrive in time, so your invitation is rescineded\n")
rescind=dead.pop()
print(rescind+", sorry, dinner is cancelled, due to late table arrival.  Please enjoy the afterlife, I'll see you then.")
rescind=dead.pop()
print(rescind+", sorry, dinner is cancelled, due to late table arrival.  Please enjoy the afterlife, I'll see you then.")
rescind=dead.pop(2)
print(rescind+", sorry, dinner is cancelled, due to late table arrival.  Please enjoy the afterlife, I'll see you then.")
rescind=dead.pop(0)
print(rescind+", sorry, dinner is cancelled, due to late table arrival.  Please enjoy the afterlife, I'll see you then.\n") #added a line to break up different parts
print(dead[0]+ ", I am pleased to let you know that despite having to shrink the dinner, we still have enough space for you to make it")
print(dead[-1]+ ", I am pleased to let you know that despite having to shrink the dinner, we still have enough space for you to make it\n") #added a line to break up different parts
del dead[0]
del dead[0]
print(dead)