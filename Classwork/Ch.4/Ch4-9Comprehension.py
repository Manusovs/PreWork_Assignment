odd = [value**3 for value in range(1,11)]
print(odd)
# This is identical to 4-8 because I have been using list comprehensions, since they seem to make sense
print(odd[1:-2])
dumb = odd [:]
print(dumb)
odd.append("odd")
dumb.append("append") 
print(odd)
print(dumb)   