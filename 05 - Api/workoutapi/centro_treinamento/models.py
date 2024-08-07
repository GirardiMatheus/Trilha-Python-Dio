from sqlalchemy import  Integer, String
from sqlalchemy.orm import Mapped, mapped_column , relationship 
from workoutapi.atleta.models import AtletaModel
from workoutapi.contrib.models import BaseModel


class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'centros_treinamento'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    propietario: Mapped[str] = mapped_column(String(30), nullable=False)
    categoria: Mapped['AtletaModel'] = relationship(back_populates='centro_treinamento')
