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
                        
            # 삭제
            # delete_node에 하위 노드가 없는 경우
            if not delete_node.left and not delete_node.right:
                # delete_node가 최상위 노드일 경우
                if not parent_node:
                    self.root = None
                    del delete_node
                # 데이터가 부모 노드의 값보다 클 경우
                elif parent_node.value > value:
                    parent_node.left = None
                    del delete_node
                # 데이터가 부모 노드의 값보다 클 경우
                else:
                    parent_node.right = None
                    del delete_node
            # delete_node에 하위 노드가 존재하는 경우
            else:
                # 오른쪽 하위 노드가 존재할 경우
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
                # 왼쪽 하위 노드가 존재할 경우
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
                # 둘 다 존재할 경우
                else:
                    change_node = delete_node.right

                    # delete_node의 자리는 오른쪽 서브 트리의 가장 왼쪽에 있는 하위 노드로 대체함.
                    # delete_node의 오른쪽 하위 노드의 왼쪽 하위 노드가 없을 경우 그대로 오른쪽 하위 노드가 change_node가 됨.
                    if not change_node.left:
                        # if not parent_node:
                        delete_node.value = change_node.value
                        delete_node.right = change_node.right
                        del change_node
                        # 2. root -> change_node, change_node.left = delete_node.left
                    else:
                        parent_change_node = None

                        # 대체할 노드를 탐색
                        while change_node.left:
                            parent_change_node = change_node
                            change_node = change_node.left
                        
                        delete_node.value = change_node.value
                        parent_change_node.left = change_node.right
                        del change_node
        else:
            print('삭제할 노드가 없음')


import random

bst = BinarySearchTree()
nums = []

for i in range(1, 100):
    random_num = random.randint(1, 100)
    nums.append(random_num)
    bst.insert(random_num)

bst.in_order_traverse(bst.root)
print('')

for n in range(len(nums)):
    random_n = random.choice(nums)
    bst.delete(random_n)
    nums.remove(random_n)

bst.in_order_traverse(bst.root)
