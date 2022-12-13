import os

from src.node.node import Node


class BinaryTree:
    def __init__(self, data=None) -> None:
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")

    tree = BinaryTree(1)
    tree.root.left = Node(18)
    tree.root.right = Node(14)
    print(tree.root)
    print(tree.root.left)
    print(tree.root.right)
