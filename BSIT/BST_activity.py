class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, data):
        if data < self.data:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.add(data)
        elif data > self.data:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.add(data)

    def display(self, node=None, level=0, prefix="(ROOT)"):
        if node == None:
            node = self
        if node:
            if level == 0:
                print(f"{prefix} |_ {node.data}")
            else:
                print(f"{prefix} |{'_' * (level + 1)}{node.data}")
            if node.left:
                self.display(node.left, level + 1, "(LEFT)")
            if node.right:
                self.display(node.right, level + 1, "(RIGHT)")
                
    def search(self, data, path=None):
        if path is None:
            path = []

        path.append(self.data)

        if self.data == data:
            print(f"Path from '{path[0]}' to '{data}': {' -> '.join(map(str, path))}")
            return True
        elif data < self.data and self.left:
            return self.left.search(data, path)
        elif data > self.data and self.right:
            return self.right.search(data, path)
        
        print(f"'{data}' not found in the tree.")
        return False

    def find_min(self): 
        current = self
        while current.left:
            current = current.left
        return current

    def delete(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.right == None:
                return self.left
            if self.left == None:
                return self.right
            
            min_larger_node = self.right.find_min()
            self.data = min_larger_node.data
            self.right = self.right.delete(min_larger_node.data)
        return self
                    
raw = input("Enter a sequence of strings (space-delimited): ")
inp = raw.split()
if inp:
    tree = TreeNode(inp[0])
    for i in inp[1:]:
        tree.add(i)

tree.display()
target = input("Enter a string to search: ")
tree.search(target)
while True:
    delete = input('Enter a string to delete in the tree: ')
    if delete.lower() == 'stop':
        break
    tree = tree.delete(delete)
    if tree:
        print('\nafter deletion: ')
        tree.display()
    else:
        print("Empty")
        break
    print('Type stop to end program')