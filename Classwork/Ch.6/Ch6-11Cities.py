cities = {"Cove" : {"country": "USA",
                    "population" : "600",
                    "fact" : "This is East of Houston, near the water"},
          "Pasadena" : {"country": "USA",
                    "population" : "25000",
                    "fact" : "There are several chemical plants here"},
          "Palestine" : {"country": "USA",
                    "population" : "2000",
                    "fact" : "This is in Texas"}}

for city, data in cities.items():
    print (city.title() + ":")
    for specific in data:
        print(specific + ":\t"+ data[specific]) # This line specific is the key, to get the values you do the data list at position specific
    
       