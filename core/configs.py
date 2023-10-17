from typing import List

from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    """configurações gerais da aplicação

    Args:
        BaseSettings (BaseSettings): 
    """
    
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://Configurar url de conexão de acordo com o banco utilizado"
    DBBaseModel = declarative_base()
    
    class Config:
        case_sensitive = True

settings = Settings()