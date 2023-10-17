import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime

from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from datetime import datetime

from models.base_model import Base
from models.usuario_tipo import UsuarioTipo
from models.perfil import Perfil

usuario_perfil = Table(
    "tb_usuario_perfil",
    Base.metadata,
    Column('id_usuario', ForeignKey("tb_usuario.id")),
    Column('id_perfil', ForeignKey("tb_perfil.id"))
)

class Usuario(Base):
    __tablename__: str = 'tb_usuario'

    id : Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(sa.String(45), nullable=False)
    nascimento: Mapped[datetime] = mapped_column(sa.DateTime, nullable=True)    
    data_criacao: Mapped[datetime] = mapped_column(sa.DateTime, nullable=False)

    id_usuario_tipo : Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey('tb_usuario_tipo.id'))
    usuarioTipo: Mapped[UsuarioTipo] = orm.relationship('UsuarioTipo', lazy='joined')
    
    perfil: Mapped[list[Perfil]] = relationship(secondary=usuario_perfil)
    
    def __repr__(self) -> str:
        return f'<Usuario: {self.nome}>'