import sqlalchemy as sa

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from datetime import datetime

from models.base_model import Base

class UsuarioTipo(Base):
    __tablename__: str = 'tb_usuario_tipo'
    
    id : Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(sa.String(45), nullable=False)
    data_criacao: Mapped[datetime] = mapped_column(sa.DateTime, nullable=False)
            
    def __repr__(self) -> str:
        return f'<Tipo de usuário: {self.nome}>'