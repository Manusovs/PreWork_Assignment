favnum = {"Paola" : [3,4],
          "Talia" : [4, 8],
          "Scott" : [4, 13, 16, 64, 64**2],
          "Sarah" : [13],
          "Tiago" : [0,1]}

for name, nums in favnum.items(): 
    print (name.title() + "'s are:") 
    print (favnum[name]) 
