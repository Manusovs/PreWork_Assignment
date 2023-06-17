def describe_city(name,country = "nowhere"):
    print(name + " is in " + country)

describe_city("Austin", "USA")
describe_city("The void")
describe_city(country = "France", name = "Paris")