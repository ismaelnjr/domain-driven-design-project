
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, declarative_base


Base = declarative_base()

# Models
class CarModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    manufacturer = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    cars = relationship("Car", back_populates="model")


class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True, autoincrement=True)
    plate = Column(String, nullable=False, unique=True)
    model_id = Column(Integer, ForeignKey('models.id'), nullable=False)
    model = relationship("CarModel", back_populates="cars")
    color = Column(String, nullable=False)
    fuel_type = Column(String, nullable=False)
    horsepower = Column(Integer, nullable=False)
    transmission = Column(String, nullable=False)
    

def init_db(db_path: str) -> Engine:
    engine = create_engine(f"sqlite:///{db_path}", echo=True)
    Base.metadata.create_all(engine)
    return engine

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()


