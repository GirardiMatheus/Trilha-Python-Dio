from typing import Annotated
from pydantic import Field
from workoutapi.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT Caos', max_length=20)]
    endereco: Annotated[str, Field(description='Endereco do centro de treinamento', example='Rua X, Q02', max_length=60)]
    propietario: Annotated[str, Field(description='Propietario do centro de treinamento', example='Carlos', max_length=30)]

