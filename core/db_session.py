import sqlalchemy as sa

from sqlalchemy.orm import Session, sessionmaker

from pathlib import Path
from typing import Optional

from sqlalchemy.future.engine import Engine

from models.base_model import Base

__engine: Optional[Engine] = None

def create_engine(sqlite: bool = False):
    global __engine
    
    if __engine:
        return
    
    if sqlite:
        arquivo_db = 'db/appblankdb.sqlite'
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)
        
        conn_str = f'sqlite:///{arquivo_db}'
        __engine = sa.create_engine(url=conn_str, echo=False, connect_args={'check_same_thread': False})
    
    else:
        conn_str = 'mariadb+mariadbconnector://root:root@192.168.0.61:3305/appblankdb'             
        __engine = sa.create_engine(url=conn_str, echo=False)
    
    return __engine

def create_session() -> Session:
    global __engine
    
    if not __engine:
        create_engine()
    
    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)
    
    session: Session = __session()
    
    return session

def create_tables() -> None:
    global __engine
    
    if not __engine:
        create_engine(sqlite=False)
        
    print(__engine)
    import models.__all_models    
    print ('Excluindo tabelas')
    Base.metadata.drop_all(__engine)
    print ('Recriando tabelas')
    Base.metadata.create_all(__engine)
    print('tabelas criadas')
    
    
    
    
