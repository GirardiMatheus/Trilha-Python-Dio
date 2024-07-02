from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from sqlalchemy import select
from workoutapi.atleta.schemas import AtletaIn, AtletaOut
from workoutapi.contrib.dependencies import DatabaseDependency
from workoutapi.atleta.models import AtletaModel
from workoutapi.categorias.models import CategoriaModel
from workoutapi.centro_treinamento.models import CentroTreinamentoModel
router = APIRouter()

@router.post(
    '/', 
    summary='Criar um novo atleta',
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaOut
)
async def post(
            db_session: DatabaseDependency, 
            atleta_in: AtletaIn = Body(...)
):
    categoria_name = atleta_in.categoria.nome
    centro_treinamento_name = atleta_in.centro_treinamento.nome
    categoria = (
        await db_session.execute(
        select(CategoriaModel).filter_by(nome=categoria_name)
        ).scalars().first()
    
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detai=f'A categoria {categoria_name} nao foi encontrada.'
            )
    centrotreinamento = (
        await db_session.execute(
        select(CentroTreinamentoModel).filter_by(nome=centro_treinamento_name)
        ).scalars().first()
    
    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detai=f'O centro de treinamento {centro_treinamento_name} nao foi encontrado.'
            )
    try:
        atleta_out = AtletaOut(
            id=uuid4(), created_at=datetime.utcnow(),
            **atleta_in.model_dump()
        )
        atleta_model = AtletaModel(
            **atleta_out.model_dump(exclude={'categoria', 'centro_treinamento'})
        )
        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento = centro_treinamento.pk_id

        db_session.add(atleta_model)
        await db_session.commit()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detai='Ocorreu um erro ao inserir os dados no banco'
            )
    return atleta_out
