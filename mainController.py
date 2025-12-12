from rectangleController import RectangleController
from circleController import CircleController
from triangleController import TriangleController
from parseText import ParseText

class Controller:

    def __init__( self ):
        self.text = ParseText("menuText.json")
        self.mainMenu()

    def mainMenu( self ):
        while True:
            print("\n" + self.text.getMenu("main_menu"))
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
                    print(self.text.getNoOption("main_menu"))

main = Controller()