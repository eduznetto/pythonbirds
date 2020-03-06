class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    Luciano = Pessoa(renzo, nome='Luciano')
    print(Pessoa.cumprimentar)
    print(id(Luciano))
    print(Luciano.cumprimentar)
    print(Luciano.nome)
    print(Luciano.idade)
    for filho in Luciano.filhos:
        print(filho.nome)
    Luciano.sobrenome ='Ramalho'
    del Luciano.filhos
    Luciano.olhos = 1
    del Luciano.olhos
    print(Luciano.__dict__)
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(Luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(Luciano.olhos),id(renzo.olhos))
    print(Pessoa.metodo_estatico(), Luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), Luciano.nome_e_atributos_de_classe())





