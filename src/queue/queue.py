from src.node.node import Node


class Queue:
    def __init__(self) -> None:
        pass

    def push(self, elem) -> None:
        pass

    def pop(self) -> None:
        pass

    def peek(self) -> None:
        pass

    def size(self) -> int:
        pass

    def __len__(self) -> int:
        return self.size()

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return "Queue"
