class BinaryTree:
    def __init__(self, root):
        self.node = root
        self.left = None
        self.right = None

    def ins_left(self, node):
        if self.left == None:
            self.left = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.left = self.left
            self.left = t

    def ins_right(self, node):
        if self.right == None:
            self.right = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.right = self.right
            self.right = t

    def get_right_node(self):
        return self.right
            
    def get_left_node(self):
        return self.left

    def set_root_val(self, obj):
        self.node = obj

    def get_root_val(self):
        return self.node


r = BinaryTree('a')
print(r.get_root_val())
print(r.get_left_node())
r.ins_left('b')
print(r.get_left_node())
print(r.get_left_node().get_root_val())

