from pydantic import validate_call

# validacao em tempo de exec
@validate_call
def soma(x: int, y: int): # gnoose typing
    return x + y


soma(4, '5a')