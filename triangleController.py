class triangleController():
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
                    pass 
                case 2:
                    pass
                case 3:
                    pass
                case _:
                    print("Nincs a választások között!Válasszon másikat.")
