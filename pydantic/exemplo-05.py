# pre-validators

from pydantic import BaseModel, field_validator, Field
from typing import Annotated

class Pedidos(BaseModel):
    ids: Annotated[list[int], Field(ge=0)]  # Garantindo que todos os itens sejam >= 0

    @field_validator('ids', mode='before') # quero validar antes do pydantic carregar / mudar os dados
    def convert_ids(cls, v):
        return v.split(',')
    
    # @field_validator('ids', each_item=True) # Esse "each_item" foi deprecated na ultima release da lib, a forma moderna agora é o Annotated acima
    # def validate_item(cls, v):
    #     if v < 0:
    #         raise ValueError('Nao pode ser negativo')
    #     return v

print(Pedidos(ids='1,2,3')) # cast automatico pra lista


# validacao por item
