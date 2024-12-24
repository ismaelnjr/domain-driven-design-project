

class CarModel:
    def __init__(self, name: str, manufacturer: str, year: int, id: int = None):
        self.id = id
        self.name = name
        self.manufacturer = manufacturer
        self.year = year

    def __repr__(self):
        return (f"CarModel(id={self.id}, name='{self.name}', manufacturer={self.manufacturer}")
