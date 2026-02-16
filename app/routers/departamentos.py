from fastapi import APIRouter, Depends
from app.services.departamento_service import DepartamentoService
from app.schemas.departamento import DepartamentoRespuesta, DepartamentoCrear, DepartamentoActualizar

router = APIRouter(
    prefix="/departamentos",
    tags=["departamentos"]
)

@router.post("/", response_model=DepartamentoRespuesta)
async def crear_depart(departamento: DepartamentoCrear, service: DepartamentoService = Depends()):
    return service.create(departamento)

@router.get("/", response_model=list[DepartamentoRespuesta])
async def read_all_departs(service: DepartamentoService = Depends()):
    return service.get_all()

@router.get("/{id}", response_model=DepartamentoRespuesta)
async def read_depart_by_id(id: int, service: DepartamentoService = Depends()):
    return service.get_by_id(id)

@router.patch("/{id}", response_model=DepartamentoRespuesta)
async def update_depart(id: int, departamento_data: DepartamentoActualizar, service: DepartamentoService = Depends()):
    return service.update(id, departamento_data)

@router.delete("/{id}", response_model=dict)
async def delete_depart(id: int, service: DepartamentoService = Depends()):
    return service.delete(id)