from repositories.sqlite_model_repository import SQLiteModelRepository
from application.services.car_service import CarService
from application.services.car_model_service import CarModelService
from domain.entities.car import Car
from domain.entities.car_model import CarModel
from domain.value_objects.car_specification import CarSpecification

if __name__ == "__main__":
    
    # Instanciando o repositório e o serviço
    repositorio = SQLiteModelRepository("carros.db")
    car_service = CarService(repositorio)
    model_service = CarModelService(repositorio)

    # Criando alguns modelos e carros
    model1 = CarModel(name="Opala", manufacturer="Chevrolet", year=1970)    
    model_service.save(model1)

    car1 = Car(plate="ABC-1234", model_id=model1.id, specification=CarSpecification(color="Preto", fuel_type="Gasolina", horsepower=100, transmission="Manual"))
    car_service.save(car1)

    # Listando os carros criados
    print(car_service.list_all())

    # Listando os modelos de carros criados
    print(model_service.list_all())