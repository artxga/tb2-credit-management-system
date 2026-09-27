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
        if (self._down_payment / self._vehicle_value) >= 0.20 and self._amount <= (self._vehicle_value - self._down_payment):
            self.approve()
            return True
        self.reject()
        return False
