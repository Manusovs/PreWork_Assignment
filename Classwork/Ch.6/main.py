# my_dict = {"awards":{"SB":"XX", "PB":[1991,1995,1996]}}
# # print (my_dict['awards']["PB"][-2])
# # print(type(my_dict['awards']["PB"][-2]))

# my_dict2 = {"name":["XX","AAA", "ZYERRT"]}
# # print ("has", len(my_dict2["name"]))

# del my_dict2["name"]
# # print(my_dict2['name'][1])
# print(my_dict2.get('name',"XXX"))

a = {"name" : "A",
     "position" : "QB",
     "team" : "Dall Co",
     "age" : 54,
     "superbowls" : ["X","XX","XXX"],
     "awards" : {"SB" : "a",
                 "probowl" : [1991, 1992, 1993, 1994, 1995, 1996],
                 "MY" : 1}}

a1 = []
for k, v in a["awards"].items():
    if k == "SB" or k == "MY":
        a1.append(v)
print(a1)
# print(a.get("awards","age")["probowl"][len(a["position"])])

# for key in a:
#     if key > "position":
#          print (key, end=" ")

# b= ["a",'b','c','d','e','f','g']
# print (b.pop(2))

# c= {"age" : 54}
# c.update({"age":14})
# print(c["age"])
