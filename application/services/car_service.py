
from domain.interfaces.model_repository_interface import ModelRepositoryInterface
from domain.entities.car import Car

class CarService:
    def __init__(self, car_repository: ModelRepositoryInterface):
        self.car_repository = car_repository

    def create_car(self, car: Car):
        car.id = self.car_repository.add_car(car)
        return car

    def get_car_by_id(self, car_id: int) -> Car:
        car = self.car_repository.get_car_by_id(car_id)
        if not car:
            raise ValueError(f"Carro com ID {car_id} não encontrado.")
        return car

    def list_cars(self) -> list[Car]:
        cars = self.car_repository.get_all_cars()
        return [car for car in cars]

    def update_car(self, car_id: int, updated_car: Car):
        car = self.car_repository.get_car_by_id(car_id)
        if not car:
            raise ValueError(f"Carro com ID {car_id} não encontrado.")
        updated_car.id = car_id
        self.car_repository.update_car(updated_car)

    def delete_car(self, car_id: int):
        car = self.car_repository.get_car_by_id(car_id)
        if not car:
            raise ValueError(f"Carro com ID {car_id} não encontrado.")
        self.car_repository.delete_car(car_id)
