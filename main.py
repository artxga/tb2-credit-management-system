from invalid_data_exception import InvalidDataException
from person import Person
from customer import Customer
from individual_customer import IndividualCustomer
from corporate_customer import CorporateCustomer
from analyst import Analyst
from installment import Installment
from payment_schedule import PaymentSchedule
from credit_application import CreditApplication
from personal_credit import PersonalCredit
from vehicle_credit import VehicleCredit
from mortgage_credit import MortgageCredit
from credit_manager import CreditManager
from console_menu import ConsoleMenu

# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    app = ConsoleMenu()
    app.run()