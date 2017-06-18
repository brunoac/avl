from binarytree import pprint, setup

def height(node):
    if node is None:
        return 0
    return node.height

class AVLNode():

    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
        self.height = 1
    
    def search(self, k):
        if k == self.key:
            return self
        
        if k > self.key:
            if self.right is None:
                return None
            return self.right.search(k)

        if self.left is None:
            return None
        return self.left.search(k)

    def insert(self, k):
        if k == self.key:
            return self

        if k > self.key:
            if self.right is None:
                self.right = AVLNode(k)
            else:
                self.right = self.right.insert(k)
        else:
            if self.left is None:
                self.left = AVLNode(k)
            else:
                self.left = self.left.insert(k)

        return self.__rebalance()
    
    def remove(self, k, parent):
        if k < self.key:
            if self.left is not None:
                self.left = self.left.remove(k, self)
        elif k > self.key:
            if self.right is not None:
                self.right = self.right.remove(k, self)
        elif self.left is not None and self.right is not None:
            self.key = self.right.__find_min()
            self.right = self.right.remove(self.key, self)
        elif parent and parent.right == self:
            if self.left is None:
                parent.right = self.right
            else:
                parent.right = self.left
            return parent.right
        elif parent and parent.left == self:
            if self.left is None:
                parent.left = self.right
            else:
                parent.left = self.left
            return parent.left

        return self.__rebalance()
        
    def __find_min(self):
        if self.left is None:
            return self.key
        return self.left.__find_min()
    
    def __rebalance(self):
        self.__update_height()
        balance = self.__balance()

        if balance > 1:
            if self.right.__balance() < 0:
                self.right = self.right.__rotate_right()
                return self.__rotate_left()
            else:
                return self.__rotate_left()

        if balance < -1:
            if self.left.__balance() > 0:
                self.left = self.left.__rotate_left()
                return self.__rotate_right()
            else:
                return self.__rotate_right()

        return self

    def __rotate_left(self):
        right_child = self.right
        self.right = right_child.left
        right_child.left = self
        self.__update_height()
        right_child.__update_height()
        return right_child

    def __rotate_right(self):
        left_child = self.left
        self.left = left_child.right
        left_child.right = self
        self.__update_height()
        left_child.__update_height()
        return left_child

    def __balance(self):
        return height(self.right) - height(self.left)

    def __update_height(self):
        self.height = max(height(self.right), height(self.left)) + 1

class AVL:

    def __init__(self):
        self.root = None

    def search(self, k):
        if self.root is None:
            return None

        return self.root.search(k)

    def insert(self, k):
        if self.root is None:
            self.root = AVLNode(k)
        else:
            self.root = self.root.insert(k)

    def remove(self, k):
        if self.root is None:
            return
        else:
            self.root = self.root.remove(k, None)

setup(
    node_init_func=lambda v: AVLNode(v),
    node_class=AVLNode,
    null_value=None,
    value_attr='key',
    left_attr='left',
    right_attr='right'
)

if __name__ == '__main__':
    avl = AVL()
    avl.insert(70)
    avl.insert(60)
    avl.insert(50)
    avl.insert(40)
    avl.insert(30)
    avl.insert(20)
    avl.insert(10)
    avl.insert(25)
    avl.insert(31)
    avl.remove(40)
    avl.remove(50)
    pprint(avl.root)
    avl.remove(25)
    pprint(avl.root)
    avl.remove(20)
    pprint(avl.root)
    avl.remove(10)
    pprint(avl.root)
    
