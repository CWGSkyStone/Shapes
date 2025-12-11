from circle import Circle
from inputData import InputData

class CircleController():    
    def __init__(self):
        self.circle = Circle()
        self.inputData = InputData()
        choice = self.menu() 
        self.getCircleResult(choice)
     
    def menu(self):
        print("\nA kört választotta!" + "\n[0.]Kilépés\n"+"[1.]Kerület\n" + "[2.]Terület\n")
        choice = self.inputData.getInteger("Válassza melyiket szeretné megtudni:\n")
        return choice
    
    def getCircleResult( self, choice ):
        match choice:
                case 0:
                    print("Kilépés ...")
                    exit()
                case 1:
                    radius = self.inputData.getFloatList(["sugár"])
                    print("\nA kör kerülete:", self.circle.calcPher(radius))  
                case 2:
                    radius = self.inputData.getFloatList(["sugár"])
                    print("\nA kör területe:", self.circle.calcArea(radius))  
                case _:
                    print("Nincs a választások között!Válasszon másikat.")