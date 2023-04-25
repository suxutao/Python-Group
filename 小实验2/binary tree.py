class Node:
    def __init__(self, val: int, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def cmp(ob: Node) -> int:
    return ob.val


class Tree:
    def __init__(self):
        self.tree_list = [Node(0)]
        self.ele_num = 0

    def add(self, val: int):
        self.add1(val)
        self.sort()

    def add1(self, val: int):
        self.tree_list.append(Node(val))
        self.ele_num += 1
        if self.ele_num == 1:
            return
        if self.ele_num % 2 == 0:
            self.tree_list[self.ele_num // 2].left = self.tree_list[self.ele_num]
        else:
            self.tree_list[self.ele_num // 2].right = self.tree_list[self.ele_num]

    # check if val is in the tree
    def find(self, val: int):
        que = Queue()
        if self.ele_num == 0:
            return False
        que.push_front(self.tree_list[1])
        while True:
            l = que.size
            for i in range(l):
                if que.queue[i].val == val:
                    return True, 
            for i in range(l):
                if que.queue[i].left is None:
                    for i in range(l, que.size):
                        if que.queue[i].val == val:
                            return True
                    return False
                que.push_front(que.queue[i].left)
                if que.queue[i].right is None:
                    for i in range(l, que.size):
                        if que.queue[i].val == val:
                            return True
                    return False
                que.push_front(que.queue[i].right)
            for i in range(l):
                que.pop(0)

    def clear(self):
        self.tree_list.clear()
        self.ele_num = 0

    # sort in the order of the index (the order of bfs)
    def sort(self):
        copy = self.tree_list[:]
        copy.sort(key=cmp)
        self.clear()
        self.tree_list.append(Node(0))
        for i in copy[1:]:
            self.add1(i.val)


class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def push_front(self, node: Node):
        self.queue.append(node)
        self.size += 1

    def pop(self, ind: int):
        self.queue.pop(ind)
        self.size -= 1
          
if __name__ == "__main__":
    tree = Tree()
    print("if you choose to find a value, input 1; else if you choose to add a value, input 2; if you want to exit, input 0 please")
    while True:
        a = int(input())
        if a == 1:
            b = int(input())
            if tree.find(b):
                print("exist")
            else:
                print("non-exist")
        elif a == 2:
            tree.add(int(input()))
            print("succeed")
        elif a == 0:
            print("over")
            break;
        else:
            print("input error")

