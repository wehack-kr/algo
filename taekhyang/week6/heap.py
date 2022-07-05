import random


class BinaryHeap(object):
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        """
        swap smallest value node to the root node percolating up
        stop if base node is smaller than parent node
        """
        last_idx = len(self)
        parent_node = last_idx // 2
        while parent_node >= 1:
            if self.items[last_idx] < self.items[parent_node]:
                self.items[last_idx], self.items[parent_node] = self.items[parent_node], self.items[last_idx]
                last_idx = parent_node
            else:
                break
            parent_node = last_idx // 2

    def insert(self, value):
        self.items.append(value)
        self._percolate_up()

    def _percolate_down(self, idx):
        """
        swap smallest value node to the root node percolating down
        """
        left = idx * 2
        right = (idx * 2) + 1
        smallest = idx

        if left > len(self) or right > len(self):
            return

        # change either left or right node with parent node if parent is greater than one of child nodes
        # 바뀐 노드 자식들만 계속 재귀적으로 비교하면서 swap 해주면 됨
        # 안바뀐 노드는 그 자식들이 모두 힙을 유지함으로 안바꿔도 됨
        if self.items[left] < self.items[smallest]:
            smallest = left

        if self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != idx:
            self.items[smallest], self.items[idx] = self.items[idx], self.items[smallest]
            self._percolate_down(smallest)

    def extract(self):
        # extract root node
        extracted = self.items[1]

        # replace 1 idx value with the last idx value
        self.items[1] = self.items[len(self)]
        self.items.pop()

        # and sort the rest of nodes under root node
        self._percolate_down(1)
        return extracted


if __name__ == '__main__':
    heap = BinaryHeap()
    for _ in range(10):
        heap.insert(random.randint(0, 10))
    print(heap.items)

    for _ in range(10):
        val = heap.extract()
        print(val)
        print(heap.items)
