# Models
# Use quando literalmente precisar validar dados, tipo entradas e saídas de uma API Rest, intercambiar JSONs, dados de Excel, manipulação em geral...

from pydantic import BaseModel


class Pessoa(BaseModel):
    nome: str
    idade: int
    # sobrenome: str
    # email: str
    # senha: str
    # ativo: bool = True  # True caso não seja passado


class Pessoas(BaseModel):
    pessoas: list[Pessoa]  # Aqui começa o poder do Pydantic

class Festa(BaseModel):
    maiores: Pessoas
    menores: Pessoas


d = {
    'maiores': {
        'pessoas': [
            {'nome': 'Fausto', 'idade': 29},
            {'nome': 'Cássia', 'idade': 25}
        ]
    },
    'menores': {
        'pessoas': [
            {'nome': 'Fausto', 'idade': 29},
            {'nome': 'Cássia', 'idade': 25}
        ]
    }
}


print(Festa(**d))

dados = [
    {
    'nome': 'Silvio Santos',
    'idade': '23',
    'sobrenome': 'Silva',
    'email': 'vito@vito',
    'senha': '123456',
    'ativo': True
    },
    {
    'nome': 'Cassia',
    'idade': '25',
    'sobrenome': 'Rocalle',
    'email': 'vito@vito',
    'senha': '123456',
    'ativo': 'False'
    }
]

grupo = Pessoas(pessoas=dados)
print(grupo)
print(grupo.pessoas[0])

