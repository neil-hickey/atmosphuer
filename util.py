# Fix Python 2.x.
try: input = raw_input
except NameError: pass

def print_options(scenes):
    print("Here are the available options:")
    print("end\tEnd Programm")
    print type(scenes)
    for i in range(1,len(scenes)):
        print(str(i)+"\t"+scenes[i])


def load_or_sample(name,loadFunc,writeFunc):
    loaded = loadFunc()
    if loaded == None:
        result = input("No "+name+" file has been found, do you want to create a sample ? [y/n] \n")
        if result == "y":
            writeFunc(True)
        loaded = loadFunc()
        if loaded == None:
            sys.exit()
    return loaded