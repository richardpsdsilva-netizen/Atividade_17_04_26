from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


Base = declarative_base()

class Serie(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    genero = Column(String)
    ano_lancamento = Column(Integer)
    produtora = Column(String,nullable=False)

    episodios = relationship("Episodio", back_populates = "serie" , cascade = "all, delete-orphan")

class Episodios(Base):
    __tablename__ = "episodios"
    id = Column(Integer , primary_key = True)
    titulo = Column(String , nullable = False)
    numero = Column(Integer)
    duracao_minutos = Column(Float)
    serie_id =  Column(Integer , ForeignKey ('serie.id'))

    serie = relationship("Serie", back_populates= "episodios")


