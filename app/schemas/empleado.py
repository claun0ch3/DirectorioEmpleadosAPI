from sqlmodel import SQLModel

class EmpleadoCrear(SQLModel):
    nombre: str
    apellido: str
    departamento_id: int
    puesto: str | None = None
    imagen: str | None = None

class EmpleadoRespuesta(EmpleadoCrear):
    id: int

class EmpleadoActualizar(SQLModel):
    nombre: str | None = None
    apellido: str | None = None
    puesto: int | None = None
    imagen: str | None = None
    departamento_id: int | None = None