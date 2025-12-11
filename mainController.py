from inputData import InputData
from rectangle import Rectangle
from triangle import Triangle
from circle import Circle
from checker import Checker

checker = Checker()
inputData = InputData()

class Controller:

    def __init__( self ):
        self.mainMenu()

    def mainMenu( self ):
        while True:
            print("\nEz a program síkidomok kerület/terület számítására alkalmas!\n" + "Készítette: Szabó József" + "\n[0.]Kilépés\n"+"[1.]Háromszög\n" + "[2.]Tégla\n" + "[3.]Kör")
            choice = inputData.getInteger("Válassza ki az adott síkidomok közül melyiknek szeretné megtudni a kerület/terület-ét:\n")
            match choice:
                case 0:
                    print("Kilépés ...")
                    exit()
                case 1:
                    self.getTriangleResult()
                case 2:
                    self.getRectangleResult()
                case 3:
                    self.getCircleResult()
                case _:
                    print("Nincs a választások között!Válasszon másikat.")
    
    def getData( self ):
        pass

    def getCircleResult( self ):
        circle = Circle()
        print("\nA kört választotta!" + "\n[0.]Kilépés\n"+"[1.]Kerület\n" + "[2.]Terület\n")
        choice = inputData.getInteger("Válassza melyiket szeretné megtudni:\n")
        match choice:
                case 0:
                    print("Kilépés ...")
                    exit()
                case 1:
                    radius = inputData.getInteger("Adja meg a kör sugarát:")
                    while checker.checkZero(radius):
                        radius = inputData.getInteger("Adja meg a kör sugarát:")
                    print("\nA kör kerülete", circle.calcPher(radius))                       
                case 2:
                    radius = inputData.getInteger("Adja meg a kör sugarát:")
                    while checker.checkZero(radius):
                        radius = inputData.getInteger("Adja meg a kör sugarát:")
                    print("\nA kör területe", circle.calcArea(radius))  
                case _:
                    print("Nincs a választások között!Válasszon másikat.")

    def getTriangleRightAngle( self ):
        pass

main = Controller()