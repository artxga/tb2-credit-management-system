from models.credit_application import CreditApplication
from models.customer import Customer

class PersonalCredit(CreditApplication):
    """Personal loan implementation."""
    def __init__(self, application_id: str, customer: Customer, amount: float, months: int, tea: float, requires_guarantor: bool):
        super().__init__(application_id, customer, amount, months, tea)
        self._requires_guarantor = requires_guarantor

    def evaluate_risk(self) -> bool:
        # Rule: Monthly income > 2000 and estimated monthly payment < 40% of income
        estimated_payment = self._amount / self._months
        if self._customer.monthly_income >= 2000 and (estimated_payment / self._customer.monthly_income) < 0.40:
            self.approve()
            return True
        self.reject()
        return False
