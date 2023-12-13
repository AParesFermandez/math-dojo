class MathDojo:
    def __init__(self):
        self.resultado = 0

    def sumar(self, *args):
        for num in args:
            self.resultado += num
        return self

    def restar(self, *args):
        for num in args:
            self.resultado -= num
        return self

md = MathDojo()

prueba1 = md.sumar(3,2).resultado
print("El resultado es:", prueba1)

prueba2 = md.sumar(8,8).restar(prueba1).resultado
print("El resultado es:", prueba2)

prueba3 = md.sumar(2,2).restar(prueba2).resultado
print("El resultado es:", prueba3)

resultado = md.sumar(5, 10).restar(3, 2).sumar(8).restar(prueba3).resultado
print("El resultado es:", resultado)  # Salida: El resultado es: 18