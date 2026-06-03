class Pilha:
    def __init__(self):
        self.itens = []

    def is_empty(self):
        return len(self.itens) == 0

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.itens.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.itens[-1]

    def size(self):
        return len(self.itens)

    def display(self):
        if self.is_empty():
            print("Histórico vazio.")
            return
        print("\n=== Histórico de Buscas ===")
        for item in reversed(self.itens):
            print(item)