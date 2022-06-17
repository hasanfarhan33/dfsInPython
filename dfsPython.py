class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val)
        inorderTraversal(root.right)

def preorderTraversal(root):
    if root:
        print(root.val)
        preorderTraversal(root.left)
        preorderTraversal(root.right)

def postorderTraversal(root):
    if root:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.val)

def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("\nInorder Traversal: ")
inorderTraversal(root)

print("\nPreorder Traversal: ")
preorderTraversal(root)

print("\nPostorder Traversal: ")
postorderTraversal(root)
