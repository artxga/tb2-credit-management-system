from models.person import Person

class Analyst(Person):
    """Represents a bank credit analyst."""
    def __init__(self, person_id: str, name: str, email: str, phone: str, employee_code: str, approval_limit: float):
        super().__init__(person_id, name, email, phone)
        self._employee_code = employee_code
        self._approval_limit = approval_limit

    def can_approve(self, amount: float) -> bool:
        return amount <= self._approval_limit

    def show_details(self) -> str:
        return f"[Analyst] {self._name} - Code: {self._employee_code}"
