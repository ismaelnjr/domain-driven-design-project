
from domain.value_objects.car_specification import CarSpecification

class Car:
    def __init__(self, plate: str, model_id: int, id: int = None, specification: CarSpecification = None):
        self.id = id
        self.plate = plate
        self.model_id = model_id
        self.specification = specification

    def __repr__(self):
        return (f"Car(id={self.id}, name='{self.plate}', model_id={self.model_id}, "
                f"specification={self.specification})")
