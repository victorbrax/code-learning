# Nativa
from dataclasses import dataclass
from pydantic import StrictInt

@dataclass
class Pessoa:
    nome: str
    idade: int

# Pydantic 
from pydantic.dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: StrictInt


p = Pessoa('Vito', '23') # Dessa forma o CAST do Pydantic não se aplica
