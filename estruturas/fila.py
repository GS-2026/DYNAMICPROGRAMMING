from typing import cast
from estruturas.linked_list import LinkedList, Node

class Fila:
    def __init__(self):
        self._lista = LinkedList()
        self._tail = None
        self._tamanho = 0

    def is_empty(self):
        return self._lista.is_empty()

    def enqueue(self, item):
        novo = Node(item)
        if self._tail is None:
            self._lista.head = novo
        else:
            self._tail.next = novo
        self._tail = novo
        self._tamanho += 1

    def dequeue(self):
        if self.is_empty():
            return None
        valor = cast(Node, self._lista.head).data
        self._lista.remove_first()
        self._tamanho -= 1
        if self._lista.is_empty():
            self._tail = None
        return valor

    def size(self):
        return self._tamanho

    def display(self):
        if self.is_empty():
            print("Fila vazia.")
            return
        print("\n=== Fila ===")
        atual = cast(Node, self._lista.head)
        while atual:
            print(atual.data)
            atual = atual.next