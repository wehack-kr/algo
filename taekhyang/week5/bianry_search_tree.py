class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BST(object):
    def __init__(self):
        self.root = None
        self.current_node = None
        self.parent_node = None
        self.change_node = None
        self.change_parent_node = None

    def insert(self, data):
        self.root = self._insert_data(self.root, data)
        return self.root is not None

    def _insert_data(self, node, data):
        if not node:
            node = Node(data)
        else:
            if data < node.data:
                node.left = self._insert_data(node.left, data)
            elif data > node.data:
                node.right = self._insert_data(node.right, data)
        return node

    def find(self, data):
        return '있음' if self._find_data(self.root, data) else '없음'

    def _find_data(self, node, data):
        if not node:
            print(f'탐색 완료, {data} 가 트리에 없음')
            return False

        if data == node.data:
            print(f'탐색 완료, {data} 가 트리에 있음')
            return True
        elif data < node.data:
            # print(f'{data}가 {node.data} 보다 작음')
            is_data_exist = self._find_data(node.left, data)
        else:
            # print(f'{data}가 {node.data} 보다 큼')
            is_data_exist = self._find_data(node.right, data)
        return is_data_exist

    def remove(self, data):
        self.current_node = self.root
        self.parent_node = self.root

        is_searched = False
        print(f'{data} 삭제시작')

        while self.current_node:
            self.in_order_traverse(self.root)
            print('')
            if data < self.current_node.data:
                self.parent_node = self.current_node
                self.current_node = self.current_node.left
            elif data > self.current_node.data:
                self.parent_node = self.current_node
                self.current_node = self.current_node.right
            else:
                is_searched = True
                break

        if not is_searched:
            print('삭제할 데이터가 트리에 없음')
            return False

        # 1. 삭제할 노드에 child 가 없는 경우 (삭제할 노드가 리프노드인 경우)
        if not self.current_node.right and not self.current_node.left:
            print('case1')
            if data < self.parent_node.data:
                self.parent_node.left = None
            else:
                self.parent_node.right = None

        # 2. 삭제할 노드에 child 가 하나 있는 경우
        # 2-1. 삭제할 노드 왼쪽에만 child 가 있는 경우
        elif self.current_node.left and not self.current_node.right:
            print('case2-1')
            if data < self.parent_node.data:
                self.parent_node.left = self.current_node.left
            else:
                self.parent_node.right = self.current_node.left

        # 2-2. 삭제할 노드 오른쪽에만 child 가 있는 경우
        elif self.current_node.right and not self.current_node.left:
            print('case2-2')
            if data < self.parent_node.data:
                self.parent_node.left = self.current_node.right
            else:
                self.parent_node.right = self.current_node.right

        # 3. 삭제할 노드 양쪽에 child 가 있는 경우
        # 삭제할 노드를 삭제할 노드 오른쪽 child 의 맨 왼쪽라인 끝 노드로 대치하는 전략
        elif self.current_node.left and self.current_node.right:
            print('case3')
            # change node 를 삭제할 노드 오른쪽으로 세팅
            self.change_parent_node = self.current_node
            self.change_node = self.current_node.right

            while self.change_node.left:
                self.change_parent_node = self.change_node
                self.change_node = self.change_node.left

            # change node 오른쪽에 child 가 있는경우
            # 1. change_node_parent 의 왼쪽에 change_node 가 있는경우
            if self.change_node.right:
                if self.change_node.data < self.change_parent_node.data:
                    self.change_parent_node.left = self.change_node.right
                else:
                    self.change_parent_node.right = self.change_node.right
            # 2. change_node_parent 의 오른쪽에 change_node 가 있는경우
            else:
                if self.change_node.data < self.change_parent_node.data:
                    self.change_parent_node.left = None
                else:
                    self.change_parent_node.right = None

            # 3-1. 삭제할 노드가 parent 노드 왼쪽에 있는경우
            if data < self.parent_node.data:
                print('case3-1')
                self.parent_node.left = self.change_node

            # 3-2. 삭제할 노드가 parent 노드 오른쪽에 있는경우
            else:
                print('case3-2')
                self.parent_node.right = self.change_node

            self.change_node.right = self.current_node.right
            self.change_node.left = self.current_node.left

        # current node 는 메모리에서 삭제, 쓸모가 없음
        del self.current_node
        return True

    def in_order_traverse(self, node):
        if not node:
            return
        self.in_order_traverse(node.left)
        print(node.data, end=' ')
        self.in_order_traverse(node.right)


def main():
    # 1부터 999 숫자 중에서 임의로 100개 추출하여 이진 트리에 입력/검색/삭제
    import random

    bst_nums = set()
    while len(bst_nums) != 100:
        bst_nums.add(random.randint(1, 999))  # 중복이라면 아예 들어가질 않음. 그래서 반복문은 100번 이상 실행될 가능성이 높음
    # 선택된 100개의 숫자를 이진 탐색트리에 입력, 루트노트는 500으로 임의로 지정
    # 1이나 999 이면 한쪽에 치우친 트리 -> 최악의 경우 (맨마지막 숫자 read) 에 O(N)
    bst = BST()
    bst.root = Node(500)
    for num in bst_nums:
        bst.insert(num)
    bst.in_order_traverse(bst.root)

    # 입력한 100개의 숫자 검색 (검색 기능 확인)
    print('랜덤 노드 탐색 시작')
    for num in bst_nums:
        if not bst.find(num):
            print("탐색 실패, 코드를 다시 짜주세요", num)

    # 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
    delete_nums = set()
    bst_nums = list(bst_nums)
    while len(delete_nums) < 100:
        delete_nums.add(bst_nums[random.randint(0, 99)])

    # 선택한 10개의 숫자를 삭제(삭제 기능확인)
    print('랜덤 노드 삭제 시작')
    for del_num in delete_nums:
        is_deleted = bst.remove(del_num)
        if not is_deleted:
            print('노드 삭제 실패, 코드를 다시 짜주세요', del_num)  # 이게 사실 나오면 코드 잘못짠것임
        bst.in_order_traverse(bst.root)
        print('')
    print('노드 삭제 완료')


if __name__ == '__main__':
    main()
