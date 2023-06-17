cube = [value**3 for value in range(1,11)]
print(cube)
# This is identical to 4-8 because I have been using list comprehensions, since they seem to make sense
# print(odd[1:-2])
# dumb = odd [:]
# print(dumb)
# odd.append("odd")
# dumb.append("append") 
# print(odd)
# print(dumb)   
print("The first 3 cubes from integers are " + str(cube[:3]))
print("3 Cubes in the middle of the list are " + str(cube[2:5]))
print("The last 3 Cubes in this list are " + str(cube[-3:]))