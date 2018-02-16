def table_print(headers, data, width):
    output = "{0:<"+str(width)+"} {1:<"+str(width)+"} {2:<"+str(width)+"} {3:<"+str(width)+"}"
    print(output.format(headers[0],headers[1],headers[2], headers[3]))

    print("-"*70)

    for entry in dinosaurs:
      print(output.format(entry[0], entry[1], entry[2], entry[3]))
    print()


labels = ["Name", "Weight in Lbs", "Description", "Period"]
dinosaurs = [["Tyrannosaurus", 16000, "carnivore", "Late Cretaceous"],
             ["Ankylosaurus", 10000, "herbivore", "Late Cretaceous"],
             ["Stegosaurus", 6000, "herbivore", "Late Jurassic"],
             ["Deinonyehus", 175, "carnivore", "Early Cretaceous"]]

table_print(labels, dinosaurs, 18)
    


def table_print(headers, data, width):
    output = "{0:<"+str(width)+"} {1:<"+str(width)+"}"
    print(output.format(headers[0],headers[1]))

    print("-"*20)

    for entry in dinosaurs:
        print(output.format(entry[0], entry[1]))

        
def table_print(headers, data, width):
    output="{:>{}} {:>{}}"
    print(output.format(headers[0], width, headers[1], width))
    
    print("-"*30)
          
    for entry in data:
        print(output.format(entry[0], width, entry[1], width))
    print()

labels = ["Nest", "Eggs"]

dinosaurList=[]
for i in range(4):
    dinoInput=input("Please enter the dinosaur's name. ")
    eggInput=input("Please enter the number of eggs found. ")
    dinosaurList.append([dinoInput, eggInput])
    print("Current fossilized dinosaur egg count.")
    print()
    table_print(labels, dinosaurList, 10)
    
