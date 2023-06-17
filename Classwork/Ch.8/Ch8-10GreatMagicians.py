
def show_magicians(name):
    for i in name:
        print(i)

def make_great(name):
    for i in range(len(name)):
        name[i] = (name[i] + " the_Great")
   


magicians = ["Houdini","Merlin"]

make_great(magicians)
show_magicians(magicians)

