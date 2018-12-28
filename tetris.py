class Position:
    def __init__(self, x, y):
        self.x, self.y = x, y
        
    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"

class Tetrimino:
    """Represent a single Tetrimino"""
    SHAPE = {'I', 'J', 'L', 'O', 'S', 'T', 'Z'}
    TILES = {'I': {Position(-2,0), Position(-1,0), Position(0,0), Position(1,0)}, 
             'J': {},
             'L': {},
             'O': {},
             'S': {},
             'T': {},
             'Z': {}}
    def __init__(self, shape, rot):
        """
        Initiate the following:
        shape: one shape from the SHAPE
        rot: 0 or 1 or 2 or 3, counterclockwisely
        tiles: set of tiles the Tetrimino occupies, with respect to a fixed center as (0,0)
        """
        pass
    
    def rotate(self):
        pass
    
    def __str__(self):
        pass
    

class Board:
    """Represent the board."""
    def __init__(self, width, height):
        """
        Initiate the following:
        width: width of board
        height: height of board
        mid: the x-coordinate of the middle grid (where the new Tetrimino appears)
        """
        pass
    
    def addtile(self, p):
        """ 
        p: Position
        Add a tile to self at position p
        """
        pass
    
    def getwidth(self):
        return self.width
    
    def getheight(self):
        return self.height
    
    @staticmethod
    def clear(b, c=0):
        """
        b: Board
        c: int, >=0
        Clear the full rows in b
        Returns a tuple (score, combo)
        score is the score received giving that there's already c combos
        combo is the new quantity of combos after this process
        """
        pass
    
    def __str__(self):
        pass

class Game:
    """Represent the current game"""
    def __init__(self):
        pass
    
    def __str__(self):
        pass
