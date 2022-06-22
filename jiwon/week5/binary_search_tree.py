"""
Binary Search Tree
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def in_order_traverse(self, node):
        if not node:
            return
        self.in_order_traverse(node.left)
        print(node.value, end=' ')
        self.in_order_traverse(node.right)

    def insert(self, value):
        if self.root:
            next_node = self.root

            while True:
                if next_node.value <= value:
                    if next_node.right:
                        next_node = next_node.right
                    else:
                        next_node.right = Node(value)
                        return
                elif next_node.value > value:
                    if next_node.left:
                        next_node = next_node.left
                    else:
                        next_node.left = Node(value)
                        return
                
        else:
            self.root = Node(value)

    def search(self, value):
        return

    def delete(self, value):
        if self.root:
            curr_node = self.root
            delete_node = None
            parent_node = None

            # 탐색
            while True:
                if not curr_node:
                    print('삭제할 노드가 없음')
                    return

                if curr_node.value == value:
                    delete_node = curr_node
                    break
                else:
                    if curr_node.value < value:
                        parent_node = curr_node
                        curr_node = curr_node.right
                    else:
                        parent_node = curr_node
                        curr_node = curr_node.left

            if not delete_node.left and not delete_node.right:
                if not parent_node:
                    self.root = None
                    del delete_node
                elif parent_node.value > value:
                    parent_node.left = None
                    del delete_node
                else:
                    parent_node.right = None
                    del delete_node
            else:
                if not delete_node.left and delete_node.right:
                    if not parent_node:
                        self.root = delete_node.right
                        del delete_node
                    elif parent_node.value > value:
                        parent_node.left = delete_node.right
                        del delete_node
                    else:
                        parent_node.right = delete_node.right
                        del delete_node
                elif not delete_node.right and delete_node.left:
                    if not parent_node:
                        self.root = delete_node.left
                        del delete_node
                    elif parent_node.value > value:
                        parent_node.left = delete_node.left
                        del delete_node
                    else:
                        parent_node.right = delete_node.left
                        del delete_node
                # 하위 노드가 여러 개 존재할 경우
                else:
                    change_node = delete_node.right

                    if not change_node.left:
                        # if not parent_node:
                        delete_node.value = change_node.value
                        delete_node.right = change_node.right
                        del change_node
                        # 2. root -> change_node, change_node.left = delete_node.left
                    else:
                        parent_change_node = None
                        while change_node.left:
                            parent_change_node = change_node
                            change_node = change_node.left
                        
                        delete_node.value = change_node.value
                        parent_change_node.left = change_node.right
                        del change_node
        else:
            print('삭제할 노드가 없음')

bst = BinarySearchTree()
bst.insert(5)
bst.insert(1)
bst.insert(8)
bst.insert(9)
bst.insert(3)
bst.insert(8)
bst.insert(6)
bst.insert(2)
bst.insert(4)
bst.insert(7)
bst.in_order_traverse(bst.root)
print()
bst.delete(10)
bst.in_order_traverse(bst.root)
