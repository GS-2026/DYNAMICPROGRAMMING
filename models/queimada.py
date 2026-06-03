class Queimada:

    def __init__(self, uc, area, ano):
        self.uc = uc
        self.area = float(str(area).replace(",", "."))
        self.ano = int(ano)

    def __str__(self):
        return f"UC: {self.uc} | Área: {self.area:.2f} ha | Ano: {self.ano}"