# sequencial = []
import os

from src.node.node import Node


class Linkedilist:
    def __init__(self):
        self.head = None
        self._size = 0

    def __repr__(self):
        arr = "["
        pointer = self.head
        for _ in range(self._size - 1):
            arr = arr + str(pointer.data) + ", "
            pointer = pointer.next
        arr = arr + str(pointer.data) + "]"
        return arr

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return self._size

    def _getnode(self, index):
        pointer = self.head
        for _ in range(index):
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
        raise ValueError(f"{elem} not in list->")

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

        while pointer.next:
            if pointer.next.data == elem:
                pointer.next = pointer.next.next
                self._size = self._size - 1
                break
            pointer = pointer.next
        else:
            raise ValueError(f"{elem} not in list->")
        return f"o {elem} foi removido com exito"

    def pop(self):
        return self.remove_last()


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")

    lista = Linkedilist()

    lista.append(7)
    lista.append(80)
    lista.append(56)
    lista.append(32)
    lista.append(17)
    print(lista)
