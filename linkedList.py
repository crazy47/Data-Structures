"""
_____________________________________________________________________________________________________
LinkedList :

   - Adding Nodes while Sortign at the same time
   - Deleting Nodes
   - Displaying linked list
_____________________________________________________________________________________________________
"""
import re


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedList:
    def __init__(self):
        self.head = None


    def updateIteration(self):
        nodes = []
        current = self.head
        if not current:
            print("Empty")
            return
        while current:
            nodes.append(str(current.data))
            current = current.next
        print(" -> ".join(nodes))



    def sortHelper(self, num): 
        newnoDE = Node(num)
        if self.head is None:
            self.head = newnoDE
            return
        if num < self.head.data:
            newnoDE.next = self.head 
            self.head = newnoDE 
            return
        current = self.head
        while current.next and current.next.data < num:
            current = current.next
        newnoDE.next = current.next
        current.next = newnoDE


    def deleter(self, num): 
        self.updateIteration()
        while self.head and self.head.data == num:
            self.head = self.head.next
        current = self.head
       


        while current and current.next: 
            if current.next.data == num:
                current.next = current.next.next 
            else:
                current = current.next
    def addSort(self, arr):
        for i in arr:
            self.sortHelper(i) 
            self.updateIteration()

    def deleteAlike(self, arr):
        for i in arr:
            self.deleter(i)
            self.updateIteration()
            
session = True

while session:

    userInput = str(input("Enter a non-sequentail, comma-delumited, list of 10 integerts: "))
    allNum = re.findall(r'-?\d+', userInput) 
    new_allNum = [int(i) for i in allNum]
    test = linkedList()
    test.addSort(new_allNum)

    toDelete = str(input("Enter a comma-delimited, lsit of integers for removeal in the list: "))
    allocatedNum = re.findall(r'-?\d+', toDelete)
    convertedNum = [int(i) for i in allocatedNum]

    test.deleteAlike(convertedNum)

    session = False