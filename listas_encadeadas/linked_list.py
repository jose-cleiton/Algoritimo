# sequencial = []
import os

from node import Node


class Linkedilist:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)

        else:
            self.head = Node(elem)
        self._size = self._size + 1

    def __len__(self):
        return self._size


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")

    lista = Linkedilist()

    lista.append(1)
    lista.append(2)
    print(lista._size)
