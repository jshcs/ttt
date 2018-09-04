import numpy as np
import copy
from utils import *
from mmtree import *
def game():
    ttt=np.ones((3,3))
    ttt=(-1)*ttt
    #print ttt
    prettyprint(ttt)
    left=[(i,j) for i in range(3) for j in range(3)]
    while True:
        if win(ttt,1):
            print "Zero wins"
            break
        if -1 not in ttt:
            print "Draw"
            break
        while True:
            row,col=int(raw_input("Row:")),int(raw_input("Col:"))
            if ttt[row,col]==-1:
                break
            else:
                print "Give another values"
        ttt[row,col]=2
        left.remove((row,col))
        if win(ttt,2):
            print "Cross wins"
            break
        if -1 not in ttt:
            print "Draw"
            break
        prettyprint(ttt)
        print "-"*10,"THINKING","-"*10
        zero_root=MMTree(ttt,True,left,row,col)
        zero_root.utility=get_utility(zero_root.ttt,True)
        get_game_tree(zero_root)
        zero_root.minimax_utility()
        zero_row,zero_col=zero_root.get_move()
        ttt[zero_row,zero_col]=1
        left.remove((zero_row,zero_col))
        if win(ttt,1):
            print "Zero wins"
            break
        if -1 not in ttt:
            print "Draw"
            break
        prettyprint(ttt)

    prettyprint(ttt)

game()
