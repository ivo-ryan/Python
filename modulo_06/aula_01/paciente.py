

def registrar(nome, idade, cpf, email):
    paciente = {'nome': nome, 'idade': idade, 'cpf': cpf, 'email': email}
    return paciente

class Paciente :
    
    def __init__(self, nome , idade, cpf, email):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        

paciente = Paciente('Ryan', 22, '000.000.000-00', 'ryan@gmail.com')

print(paciente.nome)
print(paciente.idade)
print(paciente.cpf)
print(paciente.email)

