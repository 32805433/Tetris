def easyoutput(board, score):
    """
    Output the current game to the command line
    """
    print('score='+str(score))
    d = {0: '.', 1: '#'}
    for i in range(board.getheight()):
        print(''.join([d[j] for j in board[i]]))

def output(board, score):
    pass