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

        number = int( numberStr )

        return number

    def getFloat( self,text ):

        numberStr = input( text )
        while( not re.match( "[0.-9.]+$", numberStr )):

            print( "Hibás adat!")
            numberStr = input( text )

        number = float( numberStr )

        return number