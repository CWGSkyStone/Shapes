from triangle import Triangle
from inputData import InputData
from parseText import ParseText

class TriangleController():
    def __init__(self):
        self.text = ParseText("menuText.json")
        self.triangle = Triangle()
        self.inputData = InputData()
        choice = self.menu()
        self.getTriangleResult(choice)

    def menu(self):
        print("\n" + self.text.getMenu("triangle_menu"))
        choice = self.inputData.getInteger("Válassza melyiket szeretné megtudni:\n")
        return choice

    def getTriangleResult( self, choice ):
        match choice:
                case 0:
                    print("Kilépés ...")
                    exit()
                case 1:
                    sideA, sideB, sideC = self.inputData.getFloatList(["A oldalt",  "B oldalt", "C oldalt"])
                    print("\nA háromszög kerülete:", self.triangle.calcPher(sideA,sideB,sideC))
                case 2:
                    base, height = self.inputData.getFloatList(["alapot",  "magasságot"])
                    print("\nA háromszög területe:", self.triangle.calcAreaNormal(base,height))
                case 3:
                    sideA, sideB, sideC = self.inputData.getFloatList(["A oldalt",  "B oldalt", "C oldalt"])
                    print("\nA háromszög területe (Heron):", self.triangle.calcAreaHeron(sideA,sideB,sideC))
                case _:
                    print("Nincs a választások között!Válasszon másikat.")
