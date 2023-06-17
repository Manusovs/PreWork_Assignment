Glossary = {"lower" : "lower cases all letters",
            "upper" : "upper cases all letters",
            "title" : "upper cases first letter of each word and lower cases the rest",
            "sort" : "permanently sorts items",
            "reverse" : "permanently reverse the order of items"}
for word in Glossary: 
    print(word.title() + ":\n" + Glossary[word])
    print("\n")