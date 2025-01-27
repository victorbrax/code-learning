# exemplo com JSONs

"""
Aspecto                 | field_validator                                         | model_validator                     
------------------------|---------------------------------------------------------|---------------------------------------
Foco                    | Um único campo por vez                                  | O modelo inteiro                     
Acesso a campos         | Apenas o campo atual                                    | Todos os campos                      
Contexto de execução    | Durante a validação de campos individuais               | Antes ou depois da criação do modelo  
Usos comuns             | Validar formato, tipo ou regras específicas de um campo | Validar consistência entre campos ou lógica de negócios

"""


from pydantic import BaseModel, field_validator, model_validator
import json
from typing import Optional, List

class Book(BaseModel):
    title: str
    author: str
    price: float
    publisher: str
    isbm_10: Optional[str] = None
    isbm_13: Optional[str] = None
    subtitle: Optional[str] = None

    # validando um CAMPO
    @field_validator('isbm_10') 
    @classmethod # aparentemente no pydantic v2 é required o classmethod, conferir doc
    def validate_isbm_10(cls, v):
        if not v.startswith('978'):
            print(f'O {cls.__name__} tem que comecar com 978') # poderia ser um logger
        return v
    
    # validando a MODEL
    @model_validator(mode='after')  # Validar após a instância ser criada
    def validate_title_and_isbm(cls, values):
        if values.isbm_10 and not values.isbm_10.startswith('978'):
            print(f'O livro de título "{values.title}" deve ter isbm_10 começando com "978"')
        return values

class Books(BaseModel):
    books: List[Book]

def main() -> None:
    with open('pydantic/books.json') as f:
        data = json.load(f)
        biblioteca = Books(**data)
        print(biblioteca.books[0])


# if name mas preguiça...
main()