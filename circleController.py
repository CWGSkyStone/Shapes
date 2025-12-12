from circle import Circle
from inputData import InputData
from parseText import ParseText

class CircleController():    
    def __init__(self):
        self.text = ParseText("menuText.json")
        self.circle = Circle()
        self.inputData = InputData()
        choice = self.menu() 
        self.getCircleResult(choice)
     
    def menu(self):
        print("\n" + self.text.getMenu("circle_menu"))
        choice = self.inputData.getInteger("Válassza melyiket szeretné megtudni:\n")
        return choice
    
    def getCircleResult( self, choice ):
        match choice:
                case 0:
                    print("Kilépés ...")
                    exit()
                case 1:
                    radius = self.inputData.getFloatList(["sugarat"])[0]
                    print("\nA kör kerülete:", self.circle.calcPher(radius))  
                case 2:
                    radius = self.inputData.getFloatList(["sugarat"])[0]
                    print("\nA kör területe:", self.circle.calcArea(radius))  
                case _:
                    print("Nincs a választások között!Válasszon másikat.")