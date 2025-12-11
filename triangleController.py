from triangle import Triangle
from inputData import InputData

class TriangleController():
    def __init__(self):
        self.menu()

    def menu(self):
        print("\nA háromszöget választotta!" + "\n[0.]Kilépés\n"+"[1.]Kerület\n" + "[2.]Terület\n" + "[3.]Heron terület")
        choice = self.inputData.getInteger("Válassza melyiket szeretné megtudni:\n")
        return choice

    def getTriangleResult( self, choice ):
        match choice:
                case 0:
                    print("Kilépés ...")
                    exit()
                case 1:
                    self.getData(choice) 
                case 2:
                    self.getData(choice)
                case 3:
                    self.getData(choice)
                case _:
                    print("Nincs a választások között!Válasszon másikat.")

    def getData(self, choice):
        sideA = self.inputData.getFloat("Adja meg a tégla A oldalát:")                    
        sideB = self.inputData.getFloat("Adja meg a tégla B oldalát:")
        print("\nA tégla kerülete", self.rectangle.calcArea(sideA,sideB))  
                    