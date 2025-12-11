from rectangle import Rectangle
from inputData import InputData

class RectangleController():
    def __init__(self):
        self.rectangle = Rectangle()
        self.inputData = InputData()
        choice = self.menu() 
        self.getRectangleResult(choice)
    
    def menu(self):
        print("\nA téglát választotta!" + "\n[0.]Kilépés\n"+"[1.]Kerület\n" + "[2.]Terület\n")
        choice = self.inputData.getInteger("Válassza melyiket szeretné megtudni:\n")
        return choice
    
    def getRectangleResult( self, choice ):
        match choice:
                case 0:
                    print("Kilépés ...")
                    exit()
                case 1:
                    sideA, sideB = self.inputData.getFloatList(["A oldal",  "B oldal"])
                    print("\nA tégla kerülete:", self.rectangle.calcPher(sideA,sideB))  
                case 2:
                    sideA, sideB = self.inputData.getFloatList(["A oldal",  "B oldal"])
                    print("\nA tégla területe:", self.rectangle.calcArea(sideA,sideB))  
                case _:
                    print("Nincs a választások között!Válasszon másikat.")
                    
