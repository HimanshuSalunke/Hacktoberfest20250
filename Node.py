class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return
        cur = self.root
        while True:
            if val < cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(val)
                    return
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(val)
                    return

    def search(self, val):
        cur = self.root
        while cur:
            if val == cur.val:
                return True
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return False

    def _min_node(self, node):
        cur = node
        while cur.left:
            cur = cur.left
        return cur

    def _delete(self, node, val):
        if not node:
            return node
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            temp = self._min_node(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)
        return node

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def inorder(self):
        res = []
        def dfs(n):
            if not n:
                return
            dfs(n.left)
            res.append(n.val)
            dfs(n.right)
        dfs(self.root)
        return res

    def preorder(self):
        res = []
        def dfs(n):
            if not n:
                return
            res.append(n.val)
            dfs(n.left)
            dfs(n.right)
        dfs(self.root)
        return res

    def postorder(self):
        res = []
        def dfs(n):
            if not n:
                return
            dfs(n.left)
            dfs(n.right)
            res.append(n.val)
        dfs(self.root)
        return res

def main():
    b = BST()
    for v in [50,30,20,40,70,60,80]:
        b.insert(v)
    print("Inorder", b.inorder())
    print("Preorder", b.preorder())
    print("Postorder", b.postorder())
    print("Search 40", b.search(40))
    b.delete(50)
    print("Inorder after deleting 50", b.inorder())

if __name__ == "__main__":
    main()
