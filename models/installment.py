class Installment:
    """Represents a single monthly payment installment."""
    def __init__(self, number: int, principal: float, interest: float, insurance: float, balance: float):
        self._number = number
        self._principal = round(principal, 2)
        self._interest = round(interest, 2)
        self._insurance = round(insurance, 2)
        self._total_payment = round(principal + interest + insurance, 2)
        self._balance = round(balance, 2)

    def __str__(self):
        return f"Month {self._number:02d} | Principal: ${self._principal:8.2f} | Interest: ${self._interest:8.2f} | Total: ${self._total_payment:8.2f} | Balance: ${self._balance:8.2f}"
