# Tree

트리 자료 구조는 자식 노드를 지닌 노드들로 구성된다. 첫 번째이자 가장 상위 노드를 루트 노드(Root node)라고 한다.

```js
class Node {
  constructor(data) {
    this.data = data;
    this.children = [];
  }

  add(data) {
    const node = new Node(data);
    this.children.push(node);
  }

  remove(data) {
    this.children = this.children.filter((node) => node.data !== data);
  }
}

class Tree {
  constructor() {
    this.root = null;
  }
}
```

### 예시

```js
const tree = new Tree();
tree.root = new Node(1);
tree.root.add(2);
tree.root.add(3);
console.log(tree);

tree.root.remove(2);
console.log(tree);
```

## 이진트리(Binary Tree)

이진 트리는 자식 노드가 왼쪽, 오른쪽 두개 뿐인 트리다.

```js
class BinaryTreeNode {
  constructor(data) {
    this.data = data;
    this.left = null;
    this.right = null;
  }

  add(data) {
    if (this.left === null) {
      this.left = new BinaryTreeNode(data);
    }
    if (this.right === null) {
      this.right = new BinaryTreeNode(data);
    }
  }
}

const bt = new BinaryTreeNode(1);
bt.add(2);
bt.add(3);
// bt.add(4);

console.log(bt);
```

## 이진 검색 트리(Binary Search Tree)

이진 검색 트리(BST, Binary Search Tree)도 왼쪽과 오른쪽 두 개의 자식이 있다. 하지만 이진 검색 트리의 경우, 왼쪽 자식이 부모보다 작고 오른쪽 자식이 부모보다 크다.

이진 검색 트리가 이런 구조를 지닌 이유는 검색과 삽입, 특정 값을 지닌 노드 제거의 시간 복잡도가 $O(log_2(n))$이기 때문이다. 만약 자식에 늘 부모보다 큰 숫자만 있다면 오른쪽에만 있는 불균형 이진 검색 트리가 된다. 이는 자료 구조에 큰 영향을 끼치며 삽입과 삭제, 검색의 시간 복잡도를 $O(log_2(n))$에서 $O(n)$으로 증가시킨다. 완전 균형 트리의 높이는 $log_2(n)$인 반면, 불균형 트리의 높이는 최악의 경우 $n$이 된다.

```js
class Node {
  constructor(data) {
    this.data = data;
    this.left = null;
    this.right = null;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }

  insert(data) {
    const node = new Node(data);
    if (this.root === null) {
      this.root = node;
    } else {
      this.insertNode(this.root, node);
    }
  }

  insertNode(node, newNode) {
    // 생성하려는 노드가 기존 노드의 값보다 작을 경우 왼쪽
    if (newNode.data < node.data) {
      if (this.left) {
        // left가 이미 있다면 하위에 만들기 위해 재귀
        this.insertNode(node.left, newNode);
      } else {
        // left가 없다면 거기에 생성
        node.left = newNode;
      }
    }

    // 생성하려는 노드가 기존 노드의 값보다 큰 경우 오른쪽
    if (newNode.data > node.data) {
      if (this.right) {
        this.insertNode(node.right, newNode);
      } else {
        node.right = newNode;
      }
    }
  }

  remove(data) {
    this.root = this.removeNode(this.root, data);
  }

  removeNode(node, targetData) {
    if (node === null) {
      return null;
    }

    if (targetData < node.data) {
      // 현재 바라보고 있는 노드보다 작다면 왼쪽
      node.left = this.removeNode(node.left, targetData);
      return node;
    } else if (targetData > node.data) {
      // 현재 바라보고 있는 노드보다 크다면 오른쪽
      node.right = this.removeNode(node.right, targetData);
      return node;
    } else {
      if (node.left === null && node.right === null) {
        // 현재 노드에 아무 데이터도 없을 경우
        node = null;
        return node;
      }

      if (node.left === null) {
        node = node.right;
        return node;
      } else if (node.right === null) {
        node = node.left;
        return node;
      }
    }
  }

  search(data) {
    if (this.root === null) {
      return null;
    }
    const foundNode = this.searchNode(this.root, data);
    if (foundNode.data !== data) {
      return null;
    }
    return foundNode;
  }

  searchNode(node, data) {
    if (node.data < data && node.right) {
      // 숫자가 클 경우, 오른쪽으로 탐색
      return this.searchNode(node.right, data);
    } else if (node.data > data && node.left) {
      // 숫자가 작을 경우, 왼쪽으로 탐색
      return this.searchNode(node.left, data);
    }
    return node;
  }
}
```
