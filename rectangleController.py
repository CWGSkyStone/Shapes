from rectangle import Rectangle
from inputData import InputData
from checker import Checker



class rectangleController():
    def __init__(self):
        self.rectangle = Rectangle()
        self.inputData = InputData()
        self.checker = Checker()
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
                    sideA = self.inputData.getInteger("Adja meg a tégla A oldalát:")
                    while self.checker.checkZero(sideA):
                        radius = self.inputData.getInteger("Adja meg a tégla A oldalát:")                      
                    sideB = self.inputData.getInteger("Adja meg a tégla B oldalát:")
                    while self.checker.checkZero(sideB):
                        radius = self.inputData.getInteger("Adja meg a tégla B oldalát:")     
                    print("\nA tégla kerülete", self.rectangle.calcPher(sideA,sideB))                       
                case 2:
                    sideA = self.inputData.getInteger("Adja meg a tégla A oldalát:")
                    while self.checker.checkZero(sideA):
                        radius = self.inputData.getInteger("Adja meg a tégla A oldalát:")                      
                    sideB = self.inputData.getInteger("Adja meg a tégla B oldalát:")
                    while self.checker.checkZero(sideB):
                        radius = self.inputData.getInteger("Adja meg a tégla B oldalát:")     
                    print("\nA tégla kerülete", self.rectangle.calcArea(sideA,sideB))  
                case _:
                    print("Nincs a választások között!Válasszon másikat.")
                    
test = rectangleController()