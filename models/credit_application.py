from abc import ABC, abstractmethod
from models.customer import Customer
from models.payment_schedule import PaymentSchedule
from exceptions.invalid_data_exception import InvalidDataException

class CreditApplication(ABC):
    """Abstract base class for credit applications."""
    def __init__(self, application_id: str, customer: Customer, amount: float, months: int, tea: float):
        if amount <= 0 or months <= 0:
            raise InvalidDataException("Amount and months must be strictly positive.")
        self._application_id = application_id
        self._customer = customer
        self._amount = amount
        self._months = months
        self._tea = tea
        self._status = "PENDING"  # PENDING, APPROVED, REJECTED
        self._rejection_reason = ""
        self._schedule = PaymentSchedule()

    @property
    def application_id(self) -> str: return self._application_id
    
    @property
    def customer(self) -> Customer: return self._customer
    
    @property
    def amount(self) -> float: return self._amount
    
    @property
    def status(self) -> str: return self._status
    
    @property
    def rejection_reason(self) -> str: return self._rejection_reason

    @abstractmethod
    def evaluate_risk(self) -> bool:
        """Polymorphic method to evaluate if credit is approved."""
        pass

    def approve(self):
        self._status = "APPROVED"
        self._rejection_reason = ""
        self._schedule.calculate_amortization(self._amount, self._tea, self._months)

    def reject(self, reason: str = "Reglas de riesgo no cumplidas"):
        self._status = "REJECTED"
        self._rejection_reason = reason

    def show_summary(self):
        print(f"App ID: {self._application_id} | Type: {self.__class__.__name__} | Amount: ${self._amount} | Status: {self._status}")
        if self._status == "APPROVED":
            self._schedule.show_schedule()
        elif self._status == "REJECTED":
            print(f"   -> Reason: {self._rejection_reason}")
