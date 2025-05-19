from typing import List
import tkinter as tk
class TreeNode:
    def __init__(self, data, parent=None):#i used the tree i built in past activities
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = TreeNode(data, self)# the arguments specify it so that the current node would be the parent
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = TreeNode(data, self) # "self" as parent
            else:
                self.right.insert(data)
    def inorder(self) -> list['TreeNode']:
        nodes = []
        if self.left:
            nodes.extend(self.left.inorder())
        nodes.append(self)
        if self.right:
            nodes.extend(self.right.inorder())
        return nodes

    def get_sibling(self):
        if self.parent is None: # no parent means root means no sibling
            return None
        if self.parent.left == self:#if node is left child
            return self.parent.right
        return self.parent.left#else return right
    def degree(self):
        degree = 0
        if self.left:# if you have child increment
            degree += 1
        if self.right:
            degree += 1
        return degree
    def depth(self):
        depth = 0
        node = self
        while node.parent: # while there is a parent travers it upwards
            node = node.parent
            depth += 1
        return depth
    def displayBst(self, canvas):#self would bre the root
        nodes = [(self, 400, 200, 120)] #positons root at position, the input would function as a stack starting with 500on the top
        while nodes:#while there is stuff in the stack
            node, x, y, x_offset = nodes.pop()
            if node.left:
                canvas.create_line(x, y, x - x_offset, y + 50) #creates a line that goes to the left and deeper due to argumetns
                nodes.append((node.left, x - x_offset, y + 50, x_offset // 2))# add the coordinates of the updated left child to stack
            if node.right:
                canvas.create_line(x, y, x + x_offset, y + 50)
                nodes.append((node.right, x + x_offset, y + 50, x_offset // 2))
            canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill='#E3E3E1')#uses canvas to create the oval to store data, coordinates will be updated thru each node
            canvas.create_text(x, y, text=str(node.data), font=('Arial', 12))#text to signify data
def txt(filename):# function to read txt
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        numbers = [int(line.strip()) for line in lines if line.strip()]
        root = TreeNode(numbers[0]) # the ROOT, the OMEGA, the ONE at the TOP
        for number in numbers[1:]:# from root up to the corresponding integers
            root.insert(number)
        return root
    except FileNotFoundError:
        print('File not found.')
    return None

filename = input('Enter the name of the txt file: ')
root = txt(filename)

if root: #only continues if there is a valid bst
    nodes = root.inorder()# inorder traversal of the tree
    header = f"{'Node':<8}{'Parent':<8}{'Sibling':<8}{'Left':<8}{'Right':<8}{'Degree':<8}{'Depth':<8}"#header for a guide, separated by 8 spaces
    print(header)#print it before the data
    for node in nodes:#for each node exxecute the compressef codes
        parent = node.parent.data if node.parent else "NULL"#parent should be stored from previous functions, if none then null
        sibling = node.get_sibling().data if node.get_sibling() else "NULL"# use our sibling function to find sibling number if not then null
        left = node.left.data if node.left else "NULL"#if theres a left node
        right = node.right.data if node.right else "NULL"
        degree = node.degree()#find degree of current node
        depth = node.depth()#find child amount
        print(f"{node.data:<8}{parent:<8}{sibling:<8}{left:<8}{right:<8}{degree:<8}{depth:<8}")#print each info
def main():
    #gui
    Main = tk.Tk()
    Main.title('BST')
    Main.geometry('800x800')
    #canvas
    canvas = tk.Canvas(Main, width=1000, height=1000, bg='#E3E3E1')
    canvas.pack()
    # draw gui once window is up
    if root:
        root.displayBst(canvas)
    Main.mainloop()
main()
tk.Tk