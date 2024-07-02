from typing import Annotated
from pydantic import Field, PositiveFloat
from workoutapi.contrib.schemas import BaseSchema, OutMixin
from workoutapi.categorias.schemas import CategoriaIn
from workoutapi.centro_treinamento.schemas import CentroTreinamentoAtleta


class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', examples='11122233344', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', examples=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', examples=75.5)]
    Altura: Annotated[PositiveFloat, Field(description='Altura do atleta', examples=1.75)]
    sexo: Annotated[str, Field(description='Sexo do atleta', examples='M', max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do Atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de Treinamento do Atleta')]


class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass
