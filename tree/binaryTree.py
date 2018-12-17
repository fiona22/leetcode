__author__ = 'Administrator'
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        node = Node(val)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]

            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def traverse(self):
        if self.root is None:
            return None
        q = [self.root]
        res = [self.root.val]
        while q != []:
            pop_node = q.pop(0)
            if pop_node.left is not None:
                q.append(pop_node.left)
                res.append(pop_node.left.val)

            if pop_node.right is not None:
                q.append(pop_node.right)
                res.append(pop_node.right.val)
        return res

    def preorder(self,root):
        if root is None:
            return []
        result = [root.val]
        left_val = self.preorder(root.left)
        right_val = self.preorder(root.right)
        return result + left_val + right_val

    def inorder(self,root):
        if root is None:
            return []
        result = [root.val]
        left_val = self.inorder(root.left)
        right_val = self.inorder(root.right)
        return left_val + result + right_val

    def postorder(self,root):
        if root is None:
            return []
        result = [root.val]
        left_val = self.postorder(root.left)
        right_val = self.postorder(root.right)
        return left_val + right_val + result

t = Tree()
for i in range(10):
    t.add(i)
print('traverse:',t.traverse())
print('preorder:',t.preorder(t.root))
print('inorder:',t.inorder(t.root))
print('postorder:',t.postorder(t.root))