from customer import Customer
from invalid_data_exception import InvalidDataException

class CorporateCustomer(Customer):
    """Represents a corporate/business customer."""
    def __init__(self, person_id: str, name: str, email: str, phone: str, monthly_income: float, ruc: str, company_name: str, years_in_operation: int):
        super().__init__(person_id, name, email, phone, monthly_income)
        if len(ruc) != 11:
            raise InvalidDataException("RUC must be exactly 11 characters long.")
        self._ruc = ruc
        self._company_name = company_name
        self._years_in_operation = years_in_operation

    def show_details(self) -> str:
        return f"[Corporate] {self._company_name} - RUC: {self._ruc} - Income: ${self._monthly_income}"
