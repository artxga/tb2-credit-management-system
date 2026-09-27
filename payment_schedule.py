from typing import List
from installment import Installment
from invalid_data_exception import InvalidDataException

class PaymentSchedule:
    """Manages the list of installments using French Amortization."""
    def __init__(self):
        self._installments: List[Installment] = []
        self._total_payable = 0.0

    def calculate_amortization(self, amount: float, tea: float, months: int, monthly_insurance: float = 0.0):
        if amount <= 0 or months <= 0:
            raise InvalidDataException("Amount and months must be greater than zero.")
        
        # Convert Annual Effective Rate (TEA) to Monthly Effective Rate (TEM)
        tem = ((1 + tea) ** (1/12)) - 1
        
        # French amortization formula: C = M * (i * (1+i)^n) / ((1+i)^n - 1)
        fixed_payment = amount * (tem * (1 + tem)**months) / ((1 + tem)**months - 1)
        
        balance = amount
        self._installments.clear()
        self._total_payable = 0.0

        for month in range(1, months + 1):
            interest = balance * tem
            principal = fixed_payment - interest
            balance -= principal
            
            # Avoid floating point negative zero
            if balance < 0.01: balance = 0.0 
            
            installment = Installment(month, principal, interest, monthly_insurance, balance)
            self._installments.append(installment)
            self._total_payable += installment._total_payment

    def show_schedule(self):
        for inst in self._installments:
            print(inst)
        print(f"Total Payable: ${self._total_payable:.2f}")
