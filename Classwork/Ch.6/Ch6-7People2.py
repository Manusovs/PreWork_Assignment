Paola = {"first_name":"Paola",
         'last_name' : 'Lemus',
         'city' : 'cove'}
Scott = {"first_name":"Scott",
         'last_name' : 'Manusov',
         'city' : 'cove'}
Talia = {"first_name":"Talia",
         'last_name' : 'Manusov',
         'city' : 'cove'}
People = [Paola,Scott,Talia]
for person in People:
    print(person["first_name"] + " " + person["last_name"] + " lives in " + person["city"].title())