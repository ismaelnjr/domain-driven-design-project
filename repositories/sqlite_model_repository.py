
import sqlite3
from domain.entities.car import Car
from domain.entities.car_model import CarModel
from domain.value_objects.car_specification import CarSpecification
from domain.interfaces.model_repository_interface import ModelRepositoryInterface

class SQLiteModelRepository(ModelRepositoryInterface):
    def __init__(self, db_path):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def add_car(self, car: Car):
        with self._connect() as conn:
            cursor = conn.cursor()
            if car.specification:
                cursor.execute("INSERT INTO cars (plate, model_id, color, fuel_type, horsepower, transmission) "
                               "VALUES (?, ?, ?, ?, ?, ?)", (car.plate, 
                                                             car.model_id, 
                                                             car.specification.color, 
                                                             car.specification.fuel_type, 
                                                             car.specification.horsepower, 
                                                             car.specification.transmission,))
            else:
                cursor.execute("INSERT INTO cars (plate, model_id) "
                               "VALUES (?, ?)", (car.plate, 
                                                 car.model_id,))
            conn.commit()
            return cursor.lastrowid

    def get_car_by_id(self, id: int):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, plate, model_id, color, fuel_type, horsepower, transmission "
                           "FROM cars WHERE id = ?", (id,))
            row = cursor.fetchone()
            if row:
                return Car(id=row[0], 
                           plate=row[1], 
                           model_id=row[2], 
                           specification=CarSpecification(color=row[3], 
                                                          fuel_type=row[4], 
                                                          horsepower=row[5], 
                                                          transmission=row[6]))

    def get_all_cars(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, plate, model_id, color, fuel_type, horsepower, transmission FROM cars")
            rows = cursor.fetchall()
            return [Car(id=row[0], 
                        plate=row[1], 
                        model_id=row[2], 
                        specification=CarSpecification(color=row[3], 
                                                       fuel_type=row[4], 
                                                       horsepower=row[5], 
                                                       transmission=row[6])) for row in rows]

    def delete_car(self, id: int):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM cars WHERE id = ?", (id,))
            conn.commit()

    def update_car(self, car: Car):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE CARS (plate, model_id, color, fuel_type, horsepower, transmission) "
                           "VALUES (?, ?, ?, ?, ?) "
                           "WHERE id = ?", (car.plate, 
                                            car.model_id, 
                                            car.specification.color, 
                                            car.specification.fuel_type, 
                                            car.specification.horsepower, 
                                            car.specification.transmission, 
                                            car.id,))
            conn.commit()
        
    def get_all_car_models(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, manufacturer, year FROM models")
            rows = cursor.fetchall()
            return [CarModel(id=row[0], name=row[1], manufacturer=row[2], year=row[3]) for row in rows]
    
    def delete_car_model(self, model_id: int):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM models WHERE id = ?", (model_id,))
            conn.commit()

    def update_car_model(self, model: CarModel):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE models (name, manufacturer, year) "
                           "VALUES (?, ?) WHERE id = ?", (model.name, model.manufacturer,model.year, model.id,))
            conn.commit()
    
    def add_car_model(self, model: CarModel):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO models (name, manufacturer, year) "
                           "VALUES (?, ?, ?)", (model.name, model.manufacturer, model.year))
            conn.commit()
            return cursor.lastrowid

    def get_car_model_by_id(self, model_id: int):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, manufacturer, year " 
                           "FROM models WHERE id = ?", (model_id,))
            row = cursor.fetchone()
            if row:
                return CarModel(id=row[0], name=row[1], manufacturer=row[2], year=row[3])
            return None
        
    