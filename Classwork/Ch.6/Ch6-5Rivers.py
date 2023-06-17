Rivers = {"nile" : "egypt",
          "mississippi" : "United States of America",
          "AMAZON" : "brazil"}
for river, country in Rivers.items():
    print("The " + river.title() + " run through " + country.title())