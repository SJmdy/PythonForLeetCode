from typing import List
from typing import Optional


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

    @classmethod
    def serialize(cls, head) -> List[int]:
        res = []
        cur = head
        while cur is not None:
            res.append(cur.val)
            cur = cur.next
        return res

    @classmethod
    def deserialize(cls, nums: List[int]):
        if len(nums) == 0:
            return None
        head = ListNode(val=nums[0])
        cur = head

        for n in nums[1:]:
            node = ListNode(val=n)
            cur.next = node
            cur = cur.next
        return head


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def serialize(cls, root) -> List[Optional[int]]:
        if root is None:
            return []
        layer = [root]
        r = [root.val]

        while len(layer) != 0:
            node = layer[0]
            layer = layer[1:]
            if node.left is not None:
                r.append(node.left.val)
                layer.append(node.left)
            else:
                r.append(None)
            if node.right is not None:
                r.append(node.right.val)
                layer.append(node.right)
            else:
                r.append(None)
        while True:
            tail = r.pop()
            if tail is not None:
                r.append(tail)
                break
        return r

    @classmethod
    def deserialize(cls, data: List[Optional[int]]):
        if len(data) == 0:
            return None

        root = TreeNode(x=data[0])
        layer = [root]
        index = 1

        while len(layer) != 0 and index < len(data):
            node = layer[0]
            layer = layer[1:]
            node.left = TreeNode(x=data[index]) if data[index] is not None else None
            index += 1
            if index == len(data):
                break
            node.right = TreeNode(x=data[index]) if data[index] is not None else None
            if node.left is not None:
                layer.append(node.left)
            if node.right is not None:
                layer.append(node.right)
        return root

    def pre_order(self):
        print(self.val)
        if self.left is not None:
            self.left.pre_order()
        if self.right is not None:
            self.right.pre_order()


class Node:
    def __init__(self, x: int, next, random):
        self.val = int(x)
        self.next = next
        self.random = random


