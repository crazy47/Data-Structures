class NODE:
  def __init__(self, data):
    self.data = data
    self.next = None

class LINKEDLIST():
  def __init__(self):
    self.head = None

  def add_node_with_sort(self, data):
    new_node = NODE(data)
    if self.head == None:
      self.head = new_node
    else:
      current = self.head
      if current.data > new_node.data:
        new_node.next = current
        self.head = new_node

  def display(self):
    current = self.head
    while current.next:
      current = current.next
    

      

