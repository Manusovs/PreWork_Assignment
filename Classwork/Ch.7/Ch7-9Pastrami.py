sandwich_orders = ["BLT", "Pastrami", "Meatball", "Pastrami", "Pastrami", "Tuna Salad", "Chicken Salad"]
finished_sandwiches = []
print("We have run out of Pastrami, all Pastrami sandwiches will be cancelled.")

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
while sandwich_orders:
    in_proc = sandwich_orders.pop()
    print("I made your " + in_proc + " sandwich.")
    finished_sandwiches.append(in_proc)
print("The following sandwiches were made:")
for completed in finished_sandwiches: print("\t" + completed) #print everything after all orders are completed