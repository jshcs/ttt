import numpy as np
import copy

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

class MMTree():
    def __init__(self,ttt,node,left,r,c):
        self.ttt=ttt
        self.children=[]
        self.utility=None
        self.node=node
        self.left=left
        self.child_utility=[]
        self.idx=None
        self.max_idx=None
        self.r=r
        self.c=c
        self.optimal_r=None
        self.optimal_c=None
    def prettyprint(self):
        prettyprint(self.ttt)
    def show_children(self):
        for child in self.children:
            prettyprint(child.ttt)
            child.show_children()
    def show_utility(self):
#         print self.child_utility,len(self.children)
        print len(self.child_utility)==len(self.children)
        for child in self.children:
            child.show_utility()
    def minimax_utility(self):
        if len(self.children)==0 or self.utility==0 or self.utility==1 or self.utility==-1:
            self.max_idx=self.utility
            return self.utility
        if self.node==True:
            self.max_idx=max([child.minimax_utility() for child in self.children])
            return self.max_idx
        else:
            self.max_idx=min([child.minimax_utility() for child in self.children])
            return self.max_idx
    def get_move(self):
        for child in self.children:
            if self.max_idx==child.max_idx:
                return child.r,child.c


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
        
ttt=np.ones((3,3))
ttt=(-1)*ttt
#print ttt
prettyprint(ttt)
left=[(i,j) for i in range(3) for j in range(3)]

def game():
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
