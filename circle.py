import math

class Circle:
    
    def __init__( self ):
        pass
    
    def calcPher( self, radius ):
        
        pher = radius * 2 * math.pi
        
        return pher
    def calcArea( self, radius ):
        
        area = math.pow( radius, 2 ) * math.pi
        
        return area