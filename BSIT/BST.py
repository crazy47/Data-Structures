# first action, Node will be called and have its own object which is the first index of the list
class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent # purpose -> for getting siblings
# second insert function will handle acroos the corresponding numbers inside the lsit from the first index upto the lext item
# insert function handles two condition, either the root has no left and right children or if ther have
# the function uses recursion
    def _insert(self, data) -> None:
        _ROOT = self.data
        if data < _ROOT:
            if self.left == None:
                self.left = Node(data, self)
            else:
                self.left.insert(data) # recurse
        else:
            if self.right == None:
                self.right = Node(data, self)
            else:
                self.right.insert(data) # recurse
                
    def _pre_order(self) -> list['Node']:
        return [self] + (self.left._pre_order() if self.left else []) + (self.right._pre_order() if self.right else []) 
        # pre-order: parent -> left child -> right child

    # each object in a recursive call -> CALL STACK -> pops when returning the result
    def _inorder(self) -> list['Node']:
        inorder_nodes = []
        if self.left:
            inorder_nodes.extend(self.left._inorder())
        inorder_nodes.append(self)
        if self.right:
            inorder_nodes.extend(self.right._inorder())
        return inorder_nodes
    