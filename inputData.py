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
        pattern = r"^(?!0*\.?0+$)(?:[1-9]\d*|\d*\.\d+)$"
        while( not re.match( pattern, numberStr )):

            print( "Hibás adat!")
            numberStr = input( text )

        return float( numberStr )