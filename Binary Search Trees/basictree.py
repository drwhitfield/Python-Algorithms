class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    
node = Node(10)

node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(10000)
