from exceptions.invalid_data_exception import InvalidDataException
from models.person import Person
from models.customer import Customer
from models.individual_customer import IndividualCustomer
from models.corporate_customer import CorporateCustomer
from models.analyst import Analyst
from models.installment import Installment
from models.payment_schedule import PaymentSchedule
from models.credit_application import CreditApplication
from models.personal_credit import PersonalCredit
from models.vehicle_credit import VehicleCredit
from models.mortgage_credit import MortgageCredit
from controllers.credit_manager import CreditManager
from views.console_menu import ConsoleMenu


if __name__ == "__main__":
    app = ConsoleMenu()
    app.run()