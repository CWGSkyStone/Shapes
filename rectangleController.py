from rectangle import Rectangle
from inputData import InputData
from parseText import ParseText

class RectangleController():
    def __init__(self):
        self.text = ParseText("menuText.json")
        self.rectangle = Rectangle()
        self.inputData = InputData()
        choice = self.menu() 
        self.getRectangleResult(choice)
    
    def menu(self):
        print("\n" + self.text.getMenu("rectangle_menu"))
        choice = self.inputData.getInteger("Válassza melyiket szeretné megtudni:\n")
        return choice
    
    def getRectangleResult( self, choice ):
        match choice:
                case 0:
                    print("Kilépés ...")
                    exit()
                case 1:
                    sideA, sideB = self.inputData.getFloatList(["A oldalt",  "B oldalt"])
                    print("\nA tégla kerülete:", self.rectangle.calcPher(sideA,sideB))  
                case 2:
                    sideA, sideB = self.inputData.getFloatList(["A oldalt",  "B oldalt"])
                    print("\nA tégla területe:", self.rectangle.calcArea(sideA,sideB))  
                case _:
                    print("Nincs a választások között!Válasszon másikat.")
                    
