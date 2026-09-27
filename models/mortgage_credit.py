from models.credit_application import CreditApplication
from models.customer import Customer

class MortgageCredit(CreditApplication):
    """Mortgage loan implementation."""
    def __init__(self, application_id: str, customer: Customer, amount: float, months: int, tea: float, property_value: float):
        super().__init__(application_id, customer, amount, months, tea)
        self._property_value = property_value

    def evaluate_risk(self) -> bool:
        # Rule: Max term is 300 months, Loan <= 90% of property value
        if self._months <= 300 and self._amount <= (self._property_value * 0.90):
            self.approve()
            return True
        self.reject()
        return False
