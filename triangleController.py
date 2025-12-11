from triangle import Triangle
from inputData import InputData

class TriangleController():
    def __init__(self):
        self.triangle = Triangle()
        self.inputData = InputData()
        choice = self.menu()
        self.getTriangleResult(choice)

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
                    sideA, sideB, sideC = self.inputData.getFloatList(["A oldal",  "B oldal", "C oldal"])
                    print("\nA háromszög kerülete:", self.triangle.calcPher(sideA,sideB,sideC))
                case 2:
                    base, height = self.inputData.getFloatList(["alap",  "magasság"])
                    print("\nA háromszög területe:", self.triangle.calcPher(base,height))
                case 3:
                    sideA, sideB, sideC = self.inputData.getFloatList(["A oldal",  "B oldal", "C oldal"])
                    print("\nA háromszög területe (Heron):", self.triangle.calcPher(sideA,sideB,sideC))
                case _:
                    print("Nincs a választások között!Válasszon másikat.")
