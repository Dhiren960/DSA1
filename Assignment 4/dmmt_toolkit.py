from collections import deque

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            temp = self._min_value(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        return node

    def _min_value(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, w))

    def bfs(self, start):
        visited = set()
        q = deque([start])
        order = []
        visited.add(start)
        while q:
            node = q.popleft()
            order.append(node)
            for neighbor, _ in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return order

    def dfs(self, start):
        visited = set()
        order = []
        def helper(node):
            visited.add(node)
            order.append(node)
            for neighbor, _ in self.graph[node]:
                if neighbor not in visited:
                    helper(neighbor)
        helper(start)
        return order

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

def main():
    print("DMMT TOOLKIT OUTPUT")
    print("\nBST Operations")
    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bst.insert(v)
    print("Initial Inorder:", bst.inorder())
    print("Search 20:", bst.search(20))
    print("Search 90:", bst.search(90))

    bst.delete(20)
    print("After deleting leaf node 20:", bst.inorder())

    bst.insert(65)
    bst.delete(60)
    print("After deleting node with one child 60:", bst.inorder())

    bst.delete(30)
    print("After deleting node with two children 30:", bst.inorder())

    print("\nGraph Operations")
    g = Graph()
    edges = [
        ('A','B',2), ('A','C',4), ('B','D',7), ('B','E',3),
        ('C','E',1), ('D','F',5), ('E','D',2), ('E','F',6),
        ('C','F',8)
    ]
    for u,v,w in edges:
        g.add_edge(u,v,w)

    print("Adjacency List:")
    for node in g.graph:
        print(node, "->", g.graph[node])

    print("BFS from A:", g.bfs('A'))
    print("DFS from A:", g.dfs('A'))

    print("\nHash Table Operations")
    ht = HashTable(5)
    keys = [(10,"Data1"), (15,"Data2"), (20,"Data3"), (7,"Data4"), (12,"Data5")]
    for k,v in keys:
        ht.insert(k,v)

    print("Hash Table:", ht.table)
    print("Get 10:", ht.get(10))
    print("Get 15:", ht.get(15))
    print("Get 12:", ht.get(12))

    ht.delete(15)
    print("After deleting 15:", ht.table)

if __name__ == "__main__":
    main()
