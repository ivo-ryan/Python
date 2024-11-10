class Quadrado:
    
    def __init__(self, lado):
        self.__lado = lado
        self.__area = lado * lado

    
    def retorna_area(self):
        print(self.__area)

    

quadrado = Quadrado(3)
quadrado.retorna_area()


class Aluno:
    def __init__(self, nome , idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.notas = None


aluno1 = Aluno('Ivo Ryan', '22', 2937492082)

print(aluno1.nome)
print(aluno1.idade)
print(aluno1.matricula)