from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4

from workoutapi.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOUT
from workoutapi.centro_treinamento.models import CentroTreinamentoModel
from workoutapi.contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select

router = APIRouter()

@router.post(
    '/', 
    summary='Criar um Novo Centro de Treinamento',
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoOUT,
)
async def post(
            db_session: DatabaseDependency, 
            centro_treinamento_in: CentroTreinamentoIn = Body(...)
) -> CentroTreinamentoOUT:
    centro_treinamento_out = CentroTreinamentoOUT(
        id=uuid4(), 
        **centro_treinamento_in.model_dump()
    )
    centro_treinamento_model = CentroTreinamentoModel(
        **centro_treinamento_out.model_dump()
    )
    db_session.add(centro_treinamento_model)
    await db_session.commit()
    
    return centro_treinamento_out

@router.get(
    '/',
    summary='Consultar todos os centros de treinamento',
    status_code=status.HTTP_200OK,
    response_model=list[CentroTreinamentoOUT],
)
async def query(
    db_session: DatabaseDependency,
) ->list[CentroTreinamentoOUT]:
    centros_treinamento_out: list[CentroTreinamentoOUT] = (
        await db_session.execute(select(CentroTreinamentoModel))
    ).scalars().all()

    return centros_treinamento_out

@router.get(
    '/{id}',
    summary='Consultar um Centro de Treinamento pelo id',
    status_code=status.HTTP_200OK,
    response_model=CentroTreinamentoOUT,
)
async def query(
    id: UUID4,
    db_session: DatabaseDependency,
) -> CentroTreinamentoOUT:
    centros_treinamento_out: CentroTreinamentoOUT = (
        await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))
    ).scalars.all
    
    if not centros_treinamento_out:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Centro de Treinamento não encontrado no id: {id}'
    )

    return centros_treinamento_out