from sqlmodel import Session, select
from fastapi import Depends, HTTPException
from app.models.empleado import Empleado
from app.schemas.empleado import EmpleadoCrear, EmpleadoRespuesta, EmpleadoActualizar
from app.db.session import get_session

import os
import shutil
from fastapi import UploadFile

class EmpleadoService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, empleado_data: EmpleadoCrear) -> EmpleadoRespuesta:
        empleado = Empleado(**empleado_data.model_dump())
        self.session.add(empleado)
        self.session.commit()
        self.session.refresh(empleado)
        return EmpleadoRespuesta(**empleado.model_dump())

    def get_all(self, id: int | None, nombre: str | None, apellido: str | None, puesto: str | None, imagen: str | None):
        query = select(Empleado)

        if id:
            query = query.where(Empleado.id == id)
        if nombre:
            query = query.where(Empleado.nombre == nombre)
        if apellido:
            query = query.where(Empleado.apellido == apellido)
        if puesto:
            query = query.where(Empleado.puesto == puesto)
        if imagen:
            query = query.where(Empleado.imagen == imagen)

        return self.session.exec(query).all()

    def get_by_id(self, id: int):
        empleado = self.session.get(Empleado, id)
        if not empleado:
            raise HTTPException(status_code=404, detail="Empleado no encontrado")
        return empleado

    def update(self, id: int, empleado_data: EmpleadoActualizar) -> Empleado:
        empleado = self.session.get(Empleado, id)
        if not empleado:
            raise HTTPException(status_code=404, detail="Empleado no encontrado")

        empleado_dict = empleado_data.model_dump(exclude_unset=True)
        for key, value in empleado_dict.items():
            setattr(empleado, key, value)

        self.session.add(empleado)
        self.session.commit()
        self.session.refresh(empleado)
        return empleado

    def delete(self, id: int):
        empleado = self.session.get(Empleado, id)
        if not empleado:
            raise HTTPException(status_code=404, detail="Empleado no encontrado")
        self.session.delete(empleado)
        self.session.commit()
        return {"message": "Empleado eliminado"}

    async def save_image(self, file: UploadFile) -> str:
        upload_dir = "app/static/uploads"

        # Asegura que la carpeta existe
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        # Construye la ruta del archivo
        file_path = os.path.join(upload_dir, file.filename)

        # Guarda el contenido del archivo en el servidor
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Devuelve la ruta relativa para guardar en la BD
        return f"/static/uploads/{file.filename}"