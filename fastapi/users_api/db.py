from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from .models import table_registry
from .settings import Settings


engine = create_engine(Settings().DATABASE_URL)
table_registry.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session # Ao implementar o yield, o return responsável por fechar a Session deixa de ser o da função "get_session" e passa a ser o da função da rota