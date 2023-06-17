pizzas = ["mushroom", "pineapple", "veggie supreme"]
for pizza in pizzas:
    print("Scott enjoys " + pizza + " pizza.")
print("Pizza is great, and covers several food groups, despite being considered unhealthy")
friend_pizzas = pizzas[:]
pizzas.append("white")
friend_pizzas.append("Hawaiian")
for pizza in pizzas:
    print(pizza)
print("")
for fpizza in friend_pizzas:
    print(fpizza)