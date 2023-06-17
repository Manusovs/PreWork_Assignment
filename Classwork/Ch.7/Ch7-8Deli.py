sandwich_orders = ["BLT", "Meatball", "Tuna Salad", "Chicken Salad"]
finished_sandwiches = []
while sandwich_orders:
    in_proc = sandwich_orders.pop()
    print("I made your " + in_proc + " sandwich.")
    finished_sandwiches.append(in_proc)
print("The following sandwiches were made:")
for completed in finished_sandwiches: print("\t" + completed) #print everything after all orders are completed