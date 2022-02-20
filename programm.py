import os 

folderN = os.path.join(os.path.dirname(__file__), "names")

counter = 0

files = os.listdir(folderN)
for file in files:
    print(file)
    
    with open(str(folderN) + str("/") + str(file), "r", encoding='utf-8') as data:
        for line in data:
            names = line.split()
            #print(names)
            if "Max" in names:
                counter = counter +1

            else:
                continue



print(counter)