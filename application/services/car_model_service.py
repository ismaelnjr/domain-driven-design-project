
from domain.interfaces.model_repository_interface import ModelRepositoryInterface
from domain.entities.car_model import CarModel

class CarModelService:
    def __init__(self, model_repository: ModelRepositoryInterface):
        self.model_repository = model_repository

    def save(self, car_model: CarModel):
        car_model.id = self.model_repository.add_car_model(car_model)
        return car_model

    def get_by_id(self, car_model_id: int) -> CarModel:
        car_model = self.model_repository.get_car_model_by_id(car_model_id)
        if not car_model:
            raise ValueError(f"Modelo de carro com ID {car_model_id} não encontrado.")
        return car_model

    def list_all(self) -> list[CarModel]:
        car_models = self.model_repository.get_all_car_models()
        return [car_model for car_model in car_models]

    def update(self, car_model_id: int, updated_car_model: CarModel):
        car_model = self.model_repository.get_car_model_by_id(car_model_id)
        if not car_model:
            raise ValueError(f"Modelo de carro com ID {car_model_id} não encontrado.")
        updated_car_model.id = car_model_id        
        self.model_repository.update_car_model(updated_car_model)

    def delete(self, car_model_id: int):
        car_model = self.model_repository.get_car_model_by_id(car_model_id)
        if not car_model:
            raise ValueError(f"Carro com ID {car_model_id} não encontrado.")
        self.model_repository.delete_car_model(car_model_id)
