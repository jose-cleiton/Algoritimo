import os
from src.node.node import Node


class Queue:
    def __init__(self) -> None:
        self.firs = None
        self.last = None
        self._size = 0

    def push(self, elem) -> None:
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node
        if self.firs is None:
            self.firs = node
        self._size = self._size + 1

    def pop(self) -> None:
        if self._size > 0:
            self.firs = self.firs.next
            self._size = self._size - 1
            return self.firs.data
        raise IndexError("The queue is empty")

    def peek(self) -> None:
        if self._size > 0:
            return self.firs.data
        raise IndexError("The queue is empty")

    def size(self) -> int:
        pass

    def __len__(self) -> int:
        return self._size()

    def __repr__(self) -> str:
        if self._size > 0:
            arr = ""
            pointer = self.firs
            for _ in range(self._size - 1):
                arr = arr + str(pointer.data) + " <== "
                pointer = pointer.next
            arr = arr + str(pointer.data)
            return arr
        return "Empty Queue..."

    def __str__(self) -> str:
        return self.__repr__()


if __name__ == "__main__":
    # https://www.youtube.com/watch?v=tiee9D54tE0&list=PL5TJqBvpXQv5Bb71AE5Cd_kB5rNsfU4Cp&index=12&ab_channel=Programa%C3%A7%C3%A3oDin%C3%A2mica
    os.system("cls" if os.name == "nt" else "clear")
    fila = Queue()
    fila.push('Claúdio')
    fila.push('Cleiton')
    fila.push('Cleber')
    fila.push('Caléo')
    fila.push('Cléo')
