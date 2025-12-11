from rectangleController import RectangleController
from circleController import CircleController
from triangleController import TriangleController

class Controller:

    def __init__( self ):
        self.mainMenu()

    def mainMenu( self ):
        while True:
            print("\nEz a program síkidomok kerület/terület számítására alkalmas!\n" + "Készítette: Szabó József" + "\n[0.]Kilépés\n"+"[1.]Háromszög\n" + "[2.]Tégla\n" + "[3.]Kör")
            choice = int(input("Válassza ki az adott síkidomok közül melyiknek szeretné megtudni a kerület/terület-ét:\n"))
            match choice:
                case 0:
                    print("Kilépés ...")
                    exit()
                case 1:
                    TriangleController()
                case 2:
                    RectangleController()
                case 3:
                    CircleController()
                case _:
                    print("Nincs a választások között!Válasszon másikat.")

main = Controller()