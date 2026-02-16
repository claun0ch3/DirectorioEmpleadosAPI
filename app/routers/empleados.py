from fastapi import APIRouter, Depends, Query, File, UploadFile
from app.services.empleado_service import EmpleadoService
from app.schemas.empleado import EmpleadoCrear, EmpleadoRespuesta, EmpleadoActualizar

router = APIRouter(prefix="/empleados", tags=["empleados"])

@router.post("/", response_model=EmpleadoRespuesta)
async def create_empleados(empleado: EmpleadoCrear, service: EmpleadoService = Depends()):
    return service.create(empleado)

@router.get("/", response_model=list[EmpleadoRespuesta])
async def read_all_empleados(service: EmpleadoService = Depends(),
                      id: int | None = Query(None, description="Filtrar por ID del empleado"),
                      nombre: str | None = Query(None, description="Filtrar por nombre"),
                      apellido: str | None = Query(None, description="Filtrar por apellido"),
                      puesto: str | None = Query(None, description="Filtrar por puesto"),
                      imagen: str | None = Query(None, description="Filtrar por imagen")):
    return service.get_all(id, nombre, apellido, puesto, imagen)

@router.get("/{id}", response_model=EmpleadoRespuesta)
async def read_empleado_by_id(id: int, service: EmpleadoService = Depends()):
    return service.get_by_id(id)

@router.patch("/{id}", response_model=EmpleadoRespuesta)
async def update_empleados(id: int, empleado_data: EmpleadoActualizar, service: EmpleadoService = Depends()):
    return service.update(id, empleado_data)

@router.delete("/{id}", response_model=dict)
async def delete_empleados(id: int, service: EmpleadoService = Depends()):
    return service.delete(id)

# --- NUEVO ENDPOINT PARA IMÁGENES ---
@router.patch("/{id}/image", response_model=EmpleadoRespuesta)
async def upload_empleado_image(
        id: int,
        file: UploadFile = File(...),
        service: EmpleadoService = Depends()
):
    # 1. Guardamos la imagen físicamente y obtenemos la ruta
    image_url = await service.save_image(file)

    # 2. Creamos un objeto de actualización con esa ruta
    empleado_update = EmpleadoActualizar(imagen=image_url)

    # 3. Reutilizamos tu metodo update para guardar la ruta en la BD
    return service.update(id, empleado_update)