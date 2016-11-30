#include <iostream>

class BinTreeNode(object):

    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None


        
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
  
def inorder(tree):
    order = []
    stack = [tree]
    while stack !=[]:
        if tree.left !=None and tree.left not in order: #1
            tree = tree.left
            stack.append(tree)
        else:                                               #2
            if tree.right !=None and tree.right not in order:
                order.append(tree) 
                stack.append(tree.right) 
                stack.remove(stack[len(stack)-2]) 
            else:                                   #3
                order.append(stack[len(stack)-1])
                stack.remove(stack[len(stack)-1])
            try:
                tree = stack[len(stack)-1]      #4
            except IndexError:
                pass
                            
    for i in order:
        print (i.value)
                
    #1 = checks if tree have left child ,if does add it to the stack             
    #2 = if doesn't have add tree to visited , add to stack the right child ,and pop the previous element ,who is already in visited            
    #3 =  if doesn't have any child , add the tree to visited and delete it from the stack
    #4 =  assign tree to the previous element from stack

if __name__ == '__main__':
    
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  inorder(t)
