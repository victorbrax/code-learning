# pydantic alem dos typings

# alguns dos campos:
# Constrained
# - PositiveInt, NegativeFloat
# Strinct
# - StrictInt, StrictFloat
# - valores sem conversoes
# Pydantic Types
# - EmailStr - email validator
# NameEmail - email validator
# credcard...

from pydantic import BaseModel, EmailStr

class Cadastro(BaseModel):
    email: EmailStr # pip install pydantic[email]

