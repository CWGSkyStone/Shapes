import math

class Triangle:
    
    def __init__( self ):
        pass
    
    def calcPher( self, sideA, sideB, sideC ):
        
        pher = sideA + sideB + sideC
        
        return pher
    
    def calcAreaNormal( self, base, height ):
        
        area = base * height / 2
        
        return area
    
    def calcAreaHeron( self, sideA, sideB, sideC ):
        
        s = self.calcPher( sideA, sideB, sideC ) / 2
        heronRest = (( s - sideA ) * ( s - sideB ) * ( s - sideC )) * s
        area =  math.sqrt( heronRest )
        
        return area

