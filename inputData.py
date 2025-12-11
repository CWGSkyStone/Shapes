import re

class InputData:
    
    def __init__( self ):
        pass
    

    def getString( self,text ):

        intText = input()

        return intText

    def getInteger( self,text ):

        numberStr = input( text )
        while( not re.match( "[0-9]+$", numberStr )):

            print( "Hibás adat!" )
            numberStr = input( text )

        return int( numberStr )

    def getFloat( self,text ):
        
        numberStr = input( text )
        while( not re.match( "[0.-9.]+$", numberStr )):

            print( "Hibás adat!")
            numberStr = input( text )

        return float( numberStr )
    
    def getFloatList(self, labels):
        values = []
        for label in labels:
                numberStr = input(f"Adja meg a(z) {label}-t:")
                while True:
                    try:
                        value = float(numberStr)
                        if value <= 0:
                            raise ValueError
                        values.append(value)
                        break
                    except ValueError:
                        numberStr = input(f"Hibás adat! Adja meg újra a(z) {label}-t:")

        return tuple(values)