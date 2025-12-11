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
                     self.getData(choice)
                case 2:
                    self.getData(choice)
                case _:
                    print("Nincs a választások között!Válasszon másikat.")
                    
    def getData(self,choice):
        if choice == 1:
                sideA = self.inputData.getFloat("Adja meg a tégla A oldalát:")                   
                sideB = self.inputData.getFloat("Adja meg a tégla B oldalát:")  
                print("\nA tégla kerülete", self.rectangle.calcPher(sideA,sideB))  
        elif choice == 2:
                sideA = self.inputData.getFloat("Adja meg a tégla A oldalát:")                  
                sideB = self.inputData.getFloat("Adja meg a tégla B oldalát:")    
                print("\nA tégla kerülete", self.rectangle.calcArea(sideA,sideB))  
                
