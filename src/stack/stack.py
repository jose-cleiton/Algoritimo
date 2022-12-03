# sequencial = []
import os

from src.node.node import Node

# Inserir na pilha
# Remover da Pilha
# Verificar se está vazia
# Verificar o tamanho
# Verificar o topo
# Verificar se o elemento está na pilha


class Slack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        # insere um elemento na pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    def pop(self):
        # remove o elemento do topo da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        raise IndexError("The stack is empty")

    def peek(self):
        # retorna o elemento do topo da pilha
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty")

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return False

    def is_not_empty(self):
        return not self.is_empty()

    def is_not_full(self):
        return not self.is_full()

    def is_full_or_empty(self):
        if self.is_full():
            print("Pilha cheia")
        elif self.is_empty():
            print("Pilha vazia")
            return True
        return False

    def __len__(self):
        return self._size

    def __repr__(self):
        arr = "" + " \n"
        pointer = self.top
        for _ in range(self._size - 1):
            arr = arr + "| " + str(pointer.data) + " |\n"
            pointer = pointer.next
        arr = arr + "| " + str(pointer.data) + " |\n" + "\___/" + " \n"
        return arr

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    # https://www.youtube.com/watch?v=tiee9D54tE0&list=PL5TJqBvpXQv5Bb71AE5Cd_kB5rNsfU4Cp&index=11&ab_channel=Programa%C3%A7%C3%A3oDin%C3%A2mica
    os.system("cls" if os.name == "nt" else "clear")
    pilha = Slack()
    pilha.push(1)
    pilha.push(2)
    pilha.push(3)
    pilha.push(4)
    pilha.push(5)
