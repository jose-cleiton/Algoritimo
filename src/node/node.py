class Node:
    def __init__(self, dado):
        self.data = dado    # ๐ฒ Dado a ser armazenado
        self.next = None    # ๐ Forma de apontar para outro nรณ
        self.left = None    # ๐ Forma de apontar para esquerda
        self.right = None   # ๐ Forma de apontar para direita

    def __str__(self):
        return f"Node(value={self.data}, next={self.next})"
