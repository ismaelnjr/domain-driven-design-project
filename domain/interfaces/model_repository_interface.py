
from abc import ABC, abstractmethod

class ModelRepositoryInterface(ABC):
    @abstractmethod
    def add_car(self, car):
        pass

    @abstractmethod
    def get_car_by_id(self, car_id: int):
        pass

    @abstractmethod
    def get_all_cars(self):
        pass

    @abstractmethod
    def update_car(self, car):
        pass

    @abstractmethod
    def delete_car(self, car_id: int):
        pass

    @abstractmethod
    def add_car_model(self, car_model):
        pass

    @abstractmethod
    def get_car_model_by_id(self, car_model_id: int):
        pass

    @abstractmethod
    def get_all_car_models(self):
        pass

    @abstractmethod
    def update_car_model(self, car_model):
        pass

    @abstractmethod
    def delete_car_model(self, car_model_id: int):
        pass