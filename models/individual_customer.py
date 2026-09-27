from models.customer import Customer
from exceptions.invalid_data_exception import InvalidDataException

class IndividualCustomer(Customer):
    """Represents an individual person customer."""
    def __init__(self, person_id: str, name: str, email: str, phone: str, monthly_income: float, dni: str, workplace: str):
        super().__init__(person_id, name, email, phone, monthly_income)
        if len(dni) != 8:
            raise InvalidDataException("DNI must be exactly 8 characters long.")
        self._dni = dni
        self._workplace = workplace

    def show_details(self) -> str:
        return f"[Individual] {self._name} - DNI: {self._dni} - Income: ${self._monthly_income}"
