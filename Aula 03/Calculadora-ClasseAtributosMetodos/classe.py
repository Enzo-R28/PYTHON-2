class Calculadora:
    def __init__(self, valor1, valor2): #def = metodos// self = representa o objeto
        self.valor1=valor1 #self.valor = atributo
        self.valor2=valor2
    def soma(self):
        return self.valor1 + self.valor2
    def sub(self):
        return self.valor1 - self.valor2
    def mult(self):
        return self.valor1 * self.valor2
    def div(self):
        return self.valor1 / self.valor2