from models.credit_application import CreditApplication
from models.customer import Customer

class VehicleCredit(CreditApplication):
    """Vehicle loan implementation."""
    def __init__(self, application_id: str, customer: Customer, amount: float, months: int, tea: float, vehicle_value: float, down_payment: float):
        super().__init__(application_id, customer, amount, months, tea)
        self._vehicle_value = vehicle_value
        self._down_payment = down_payment

    def evaluate_risk(self) -> bool:
        # Rule: Down payment must be at least 20% of the vehicle value
        if (self._down_payment / self._vehicle_value) < 0.20:
            self.reject(f"Cuota inicial (${self._down_payment:.2f}) es menor al 20% del valor del vehículo (${self._vehicle_value:.2f}).")
            return False
            
        if self._amount > (self._vehicle_value - self._down_payment):
            self.reject(f"Monto solicitado (${self._amount:.2f}) excede el restante a financiar (${self._vehicle_value - self._down_payment:.2f}).")
            return False
            
        self.approve()
        return True
