from typing import cast
from estruturas.linked_list import LinkedList, Node


class Pilha:
    def __init__(self):
        self._lista = LinkedList()
        self._tamanho = 0

    def is_empty(self):
        return self._lista.is_empty()

    def push(self, item):
        self._lista.insert_at_start(item)
        self._tamanho += 1

    def pop(self):
        if self.is_empty():
            return None
        topo = cast(Node, self._lista.head).data
        self._lista.remove_first()
        self._tamanho -= 1
        return topo

    def peek(self):
        if self.is_empty():
            return None
        return cast(Node, self._lista.head).data

    def size(self):
        return self._tamanho

    def display(self):
        if self.is_empty():
            print("Histórico vazio.")
            return
        print("\n=== Histórico de Buscas ===")
        atual = cast(Node, self._lista.head)
        while atual:
            print(atual.data)
            atual = atual.next