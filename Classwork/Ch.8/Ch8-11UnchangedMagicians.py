def show_magicians(name):
    for i in name:
        print(i)

def make_great(name[:]): I'm not sure why this slice notation doesn't create a copy of the list to work with.  
    for i in range(len(name)):
        name[i] = (name[i] + " the_Great")
    print(name)


magicians = ["Houdini","Merlin","someone"]

make_great(magicians)
show_magicians(magicians)

