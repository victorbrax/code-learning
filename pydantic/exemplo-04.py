from pydantic import BaseModel, field_validator


class Cadastro(BaseModel):
    email: str 
    senha_1: str
    senha_2: str

    @field_validator('email')
    def email_deve_ter_arroba(cls, v):
        # v é o valor passado no load
        if '@' not in v:
            raise ValueError('Tem que ter arroba pow')
        return v
    
    @field_validator('senha_1', 'senha_2') # apenas pra mostrar q ele aceita varios campos de uma vez
    def senhas_maiores_q_10(cls, v):
        if len(v) < 10:
            raise ValueError('Tem que ter mais de 10 na senha vei')
        return v

    # @field_validator('*')
    # def valida_tudo(cls, v):
        ... # possibilidade foda pra todos os fields

    @field_validator('senha_2') # possibilidade estendendo a parada
    def senhas_iguais(cls, v, info):
        senha_1 = info.data.get('senha_1')
        if senha_1 is not None and v != senha_1:
            raise ValueError('Senhas diferentes')
        return v
        


# Cadastro(**{'email': 'joao', 'senha_1': '123', 'senha_2': '123'})

# gerando um JSON:
json = Cadastro(**{'email': 'joa@aao', 'senha_1': '12345678910', 'senha_2': '12345678910'}).model_dump_json()
print(json)