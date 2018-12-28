def value(board, next=None, next2=None, hold=None, combo=0):
    """
    board: Board
    next, next2, hold: Tetrimino
    combo: int
    Returns an int indicates how good the situation is. Larger 
    output means better game situation.
    """
    pass

def opt_move(board, next, next2=None, hold=None, combo=0):
    """
    board: Board
    next, next2, hold: Tetrimino
    combo: int
    Returns a tuple (newboard, newcombo, move, score), where 
    newboard, newcombo are the board and combo after the optimal 
    move, move is a string consist of 'u'(up), 'd'(down), 'l'(left), 
    'r'(right), 's'(space), 'h'(hold) represent the optimal move, 
    and score is the score earned by this move.
    """
    def possible_move(board, next):
        """
        board: Board
        next: Tetrimino
        Returns a list consist of some tuples (newboard, newcombo, 
        move, score)
        """
        pass
    opt = 0
    res = None
    for t in possible_move(board, next):
        v = value(t[0], next=next2, hold=hold, combo=t[1])
        if v > opt:
            opt = v
            res = t
    if hold != None:
        for t in possible_move(board, hold):
            v = value(t[0], next=next2, hold=next, combo=t[1])
            if v > opt:
                opt = v
                res = t
    return res