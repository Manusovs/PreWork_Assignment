def make_shirt(size = "Large",text = "I love python"):
    print("We need a size " + size + " t-shirt that says " + text + ".")

make_shirt("XXL", "I love my kids")
make_shirt(text="I love my kids",size="XXL")
make_shirt()
make_shirt("Medium")