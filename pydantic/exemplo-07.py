# o pydantic tambem tem um campo generico, que vc pode configurar como achar melhor e nao necessariamente criar um validador
# (apesar de começar com F maiusculo, é uma function...)


from decimal import Decimal
from pydantic import BaseModel, Field
from datetime import datetime

class Pedido(BaseModel):
    #  pra tornar esse campo obrigatório, é uma loucura
    # imagine: se não for required, o campo vai virar 1 real..
    # entao tem que adicionar ELIPISIS na parada, pra virar erquired..
    valor_pedido: Decimal = Field(..., gt=1.00)
    criado_em: datetime = Field(default=datetime.now())
    # caso nao fosse erquired e quisesse um default
    # valor_pedido: Decimal = Field(Decimal(1.2), gt=1.00)
    # criado_em: datetime = ... # required

p = Pedido(valor_pedido=1.01)
print(p)