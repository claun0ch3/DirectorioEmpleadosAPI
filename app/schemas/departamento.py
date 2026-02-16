from sqlmodel import SQLModel

class DepartamentoCrear(SQLModel):
    nombre: str

class DepartamentoRespuesta(DepartamentoCrear):
    id: int

class DepartamentoActualizar(SQLModel):
    nombre: str | None = None