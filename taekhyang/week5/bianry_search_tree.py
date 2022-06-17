class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BST(object):
    def __init__(self):
        self.root = None
        self.current_node = None

    def insert(self, data):
        self.root = self._insert_data(self.root, data)

    def _insert_data(self, node, data):
        if not node:
            node = Node(data)
            return node

        if data < node.data:
            node.left = self._insert_data(node.left, data)
        elif data > node.data:
            node.right = self._insert_data(node.right, data)
        return node

    def find(self, data):
        return '있음' if self._find_data(self.root, data) else '없음'

    def _find_data(self, node, data):
        if not node:
            print(f'{data} 가 트리에 없음')
            return False

        if data == node.data:
            print(f'{data} 가 트리에 있음')
            return True
        elif data < node.data:
            print(f'{data}가 {node.data} 보다 작음')
            is_data_exist = self._find_data(node.left, data)
        else:
            print(f'{data}가 {node.data} 보다 큼')
            is_data_exist = self._find_data(node.right, data)
        return is_data_exist


if __name__ == '__main__':
    bst = BST()
    bst.root = Node(5)
    bst.insert(3)
    bst.insert(6)
    bst.insert(1)
    bst.insert(1)

    is_exist = bst.find(-1)
    print(is_exist)
