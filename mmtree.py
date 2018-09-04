import numpy as np
import copy
from utils import *
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
