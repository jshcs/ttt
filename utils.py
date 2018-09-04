import numpy as np
import copy
from mmtree import *

def win(ttt,num):
    zero_map=np.array([num,num,num])

    # diagonal
    if np.array_equal(np.diag(ttt),zero_map) or np.array_equal(np.diag(np.fliplr(ttt)),zero_map):
        #print "Diagonal"
        return True

    for i in range(ttt.shape[0]):
        # row
        if np.array_equal(ttt[i,:],zero_map):
            #print "Row"
            return True
        # col
        if np.array_equal(ttt[:,i],zero_map):
            #print "Col"
            return True

    return False

#win(ttt,2)

# print ttt
# ttt[0,2]=2
# ttt[1,2]=1
def prettyprint(ttt):
    res=np.chararray(ttt.shape)
    for i in range(ttt.shape[0]):
        for j in range(ttt.shape[1]):
            if ttt[i,j]==1:
                res[i,j]="O"
            elif ttt[i,j]==2:
                res[i,j]="X"
            elif ttt[i,j]==-1:
                res[i,j]="-"
    print res
# prettyprint(ttt)

def other(num):
    if num==1:
        return 2
    elif num==2:
        return 1


def get_utility(ttt,state):
    w1=win(ttt,1)
    w2=win(ttt,2)
    if w1:
        return 1
    elif w2:
        return -1
    elif not w1 and not w2:
        if -1 not in ttt:
            return 0
        else:
            if state==True:
                return 100
            else:
                return -100

def get_game_tree(root):
    for (r,c) in root.left:
        tmp_state=copy.deepcopy(root.ttt)
        if root.node==True:
            curr_node=False
            tmp_state[r,c]=1
            tmp_left=copy.deepcopy(root.left)
            tmp_left.remove((r,c))
            new_node=MMTree(tmp_state,curr_node,tmp_left,r,c)
            new_node.utility=get_utility(new_node.ttt,curr_node)
#             print new_node.utility
            new_node.idx=root.left.index((r,c))
            root.children.append(new_node)
            root.child_utility.append(new_node.utility)
            get_game_tree(new_node)
        else:
            curr_node=True
            tmp_state[r,c]=2
            tmp_left=copy.deepcopy(root.left)
            tmp_left.remove((r,c))
            new_node=MMTree(tmp_state,curr_node,tmp_left,r,c)
            new_node.utility=get_utility(new_node.ttt,curr_node)
#             print new_node.utility
            new_node.idx=root.left.index((r,c))
            root.children.append(new_node)
            root.child_utility.append(new_node.utility)
            get_game_tree(new_node)
