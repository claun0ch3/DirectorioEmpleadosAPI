from sqlmodel import Session, select
from fastapi import Depends, HTTPException
from app.models.departamento import Departamento
from app.schemas.departamento import DepartamentoCrear, DepartamentoRespuesta, DepartamentoActualizar
from app.db.session import get_session

class DepartamentoService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, departamento_data: DepartamentoCrear) -> DepartamentoRespuesta:
        departamento = Departamento(**departamento_data.model_dump())
        self.session.add(departamento)
        self.session.commit()
        self.session.refresh(departamento)
        return DepartamentoRespuesta(**departamento.model_dump())

    def get_all(self):
        return self.session.exec(select(Departamento)).all()

    def get_by_id(self, id: int):
        return self.session.get(Departamento, id)

    def update(self, id: int, departamento_data: DepartamentoActualizar) -> Departamento:
        departamento = self.session.get(Departamento, id)
        if not departamento:
            raise HTTPException(status_code=404, detail="Departamento no encontrado")

        departamento_dict = departamento_data.model_dump(exclude_unset=True)
        for key, value in departamento_dict.items():
            setattr(departamento, key, value)

        self.session.add(departamento)
        self.session.commit()
        self.session.refresh(departamento)
        return departamento

    def delete(self, id: int):
        departamento = self.session.get(Departamento, id)
        if not departamento:
            raise HTTPException(status_code=404, detail="Departamento no encontrado")
        self.session.delete(departamento)
        self.session.commit()
        return {"message": "Departamento eliminado exitosamente"}