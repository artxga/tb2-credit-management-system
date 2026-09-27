from models.person import Person
from exceptions.invalid_data_exception import InvalidDataException

class Customer(Person):
    """Base class for bank customers."""
    def __init__(self, person_id: str, name: str, email: str, phone: str, monthly_income: float):
        super().__init__(person_id, name, email, phone)
        if monthly_income < 0:
            raise InvalidDataException("Monthly income cannot be negative.")
        self._monthly_income = monthly_income
        self._credit_history = "PENDING"
    
    @property
    def monthly_income(self) -> float: return self._monthly_income
