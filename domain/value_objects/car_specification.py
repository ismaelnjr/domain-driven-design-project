
class CarSpecification:
    def __init__(self, color: str, fuel_type: str, horsepower: int, transmission: str):
        self._validate(color, fuel_type, horsepower, transmission)
        self.color = color
        self.fuel_type = fuel_type
        self.horsepower = horsepower
        self.transmission = transmission

    @staticmethod
    def _validate(color: str, fuel_type: str, horsepower: int, transmission: str):
        if not color:
            raise ValueError("A cor não pode ser vazia.")
        if fuel_type not in ['Gasolina', 'Diesel', 'Elétrico', 'Híbrido']:
            raise ValueError("Tipo de combustível inválido.")
        if horsepower <= 0:
            raise ValueError("A potência deve ser maior que zero.")
        if transmission not in ['Manual', 'Automática']:
            raise ValueError("Tipo de transmissão inválido.")

    def __repr__(self):
        return (f"CarSpecification(color='{self.color}', fuel_type='{self.fuel_type}', "
                f"horsepower={self.horsepower}, transmission='{self.transmission}')")
    
