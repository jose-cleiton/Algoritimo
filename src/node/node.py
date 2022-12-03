class Node:
    def __init__(self, dado):
        self.data = dado  # 🎲 Dado a ser armazenado
        self.next = None  # 👉 Forma de apontar para outro nó

    def __str__(self):
        return f"Node(value={self.data}, next={self.next})"
