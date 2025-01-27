# alias
from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    name: str = Field(alias="user_name")

# Exemplo de entrada JSON
json_data = {"user_name": "João Víctor"}

# Criando a instância do modelo
user = UserSchema(**json_data)

print(user.name)  # Output: João Víctor
print(user.model_dump(by_alias=True))  # Output: {'user_name': 'João Víctor'}
