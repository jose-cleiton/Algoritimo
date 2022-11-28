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

    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("<-list index out of range->")

        return pointer

    def set(self, index, elem):
        pass

    def __getitem__(self, index):
        pointer = self._getnode(index)
        if pointer:
            return pointer.data

        raise IndexError("<-list index out of range->")

    def __setitem__(self, index, elem):
        pointer = self._getnode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("<-list index out of range->")

    def index(self, elem):
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i + 1
        raise ValueError("{} not in list->".format(elem))

    def insert(self, index, elem):
        if index == 0:
            node = Node(elem)
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index - 1)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")

    lista = Linkedilist()

    lista.append(1)
    lista.append(2)
    print(lista.index(2))
    print(len(lista))
    lista.insert(0, 3)
    print(lista.index(3))
    print(lista[0])
