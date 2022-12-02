# sequencial = []
import os

from node import Node


class Linkedilist:
    def __init__(self):
        self.head = None
        self._size = 0

    def __str__(self):
        return f"LinkedList(len={self._size}, value={self.head})"

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

    def insert_start(self, node):
        node.next = self.head
        self.head = node

    def insert_in_the_index(self, index, node):
        pointer = self._getnode(index - 1)
        node.next = pointer.next
        pointer.next = node

    def append(self, elem):
        self.insert(self._size, elem)

    def insert(self, index, elem):
        node = Node(elem)

        if index == 0:
            self.insert_start(node)
        else:
            self.insert_in_the_index(index, node)
        self._size = self._size + 1

    def remove_first(self):
        value_to_be_removed = self.head.data
        if value_to_be_removed:
            self.head = self.head.next
            self._size = self._size - 1
            value_to_be_removed = None
        return value_to_be_removed

    def remove_last(self):
        pointer = self.head
        while pointer.next.next:
            pointer = pointer.next
        value_to_be_removed = pointer.next.data
        pointer.next = None
        self._size = self._size - 1
        return value_to_be_removed

    def remove(self, elem):
        pointer = self.head
        if pointer.data == elem:
            self.remove_first()
            return f"o {elem} foi removido com exito"
        else:
            while pointer.next:
                if pointer.next.data == elem:
                    pointer.next = pointer.next.next
                    self._size = self._size - 1
                    break
                pointer = pointer.next
            else:
                raise ValueError("{} not in list->".format(elem))
            return True

    def remove_at(self, index):
        if self.head == None:
            raise IndexError("<-list index out of range->")
        pointer = self.head
        if index == 0:
            self.remove_first()
            return f"o indice{index},  foi removido com exito"
        else:
            for i in range(index - 1):
                pointer = pointer.next
            value_to_be_removed = pointer.next.data
            pointer.next = pointer.next.next
            self._size = self._size - 1
            return value_to_be_removed

    def pop(self, index=None):
        if index == None:
            return self.remove_last()
        else:
            return self.remove_at(index)


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")

    lista = Linkedilist()

    lista.append(7)
    lista.append(80)
    lista.append(56)
    lista.append(32)
    lista.append(17)
