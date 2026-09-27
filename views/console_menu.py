import uuid
from controllers.credit_manager import CreditManager
from models.individual_customer import IndividualCustomer
from models.personal_credit import PersonalCredit
from exceptions.invalid_data_exception import InvalidDataException

class ConsoleMenu:
    """Handles CLI User Interface."""
    def __init__(self):
        self._manager = CreditManager()

    def _get_string_input(self, prompt: str) -> str:
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("Input cannot be empty. Please try again.")

    def _get_float_input(self, prompt: str) -> float:
        while True:
            try:
                return float(self._get_string_input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def _get_int_input(self, prompt: str) -> int:
        while True:
            try:
                return int(self._get_string_input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def _select_customer(self):
        customers = self._manager.get_customers()
        if not customers:
            print("Please register a customer first.")
            return None
            
        print("\n--- Select Customer ---")
        for i, cust in enumerate(customers, 1):
            print(f"{i}. {cust.name} (ID: {cust.person_id})")
        
        while True:
            cust_idx = self._get_int_input("Select customer number (0 to cancel): ")
            if cust_idx == 0:
                return None
            if 1 <= cust_idx <= len(customers):
                return customers[cust_idx - 1]
            print("Invalid selection. Please select a valid number.")

    def run(self):
        while True:
            print("\n--- CREDIT MANAGEMENT SYSTEM ---")
            print("1. Register Customer")
            print("2. List Customers")
            print("3. Create Personal Credit App")
            print("4. Evaluate Application")
            print("5. List Approved Applications")
            print("6. List Unapproved Applications")
            print("7. Exit")
            choice = input("Select an option: ").strip()

            try:
                if choice == '1':
                    print("\n--- Register Customer ---")
                    person_id = f"C-{uuid.uuid4().hex[:6].upper()}"
                    name = self._get_string_input("Enter Name: ")
                    email = self._get_string_input("Enter Email: ")
                    phone = self._get_string_input("Enter Phone: ")
                    monthly_income = self._get_float_input("Enter Monthly Income: ")
                    dni = self._get_string_input("Enter DNI (8 digits): ")
                    workplace = self._get_string_input("Enter Workplace: ")
                    
                    cust = IndividualCustomer(person_id, name, email, phone, monthly_income, dni, workplace)
                    self._manager.add_customer(cust)
                    print(f"Customer registered successfully con ID: {person_id}")
                elif choice == '2':
                    print("\n--- List Customers ---")
                    customers = self._manager.get_customers()
                    if not customers:
                        print("No customers registered.")
                    else:
                        for cust in customers:
                            print(f"- {cust.name} | ID: {cust.person_id} | Income: {cust.monthly_income}")
                elif choice == '3':
                    customer = self._select_customer()
                    if not customer:
                        continue
                        
                    print("\n--- Create Personal Credit App ---")
                    print(f"Creating app for customer: {customer.name}")
                    app_id = f"APP-{uuid.uuid4().hex[:6].upper()}"
                    amount = self._get_float_input("Enter Amount: ")
                    months = self._get_int_input("Enter Months: ")
                    tea = self._get_float_input("Enter TEA (e.g. 0.15 for 15%): ")
                    req_guarantor_input = self._get_string_input("Requires guarantor? (y/n): ").lower()
                    requires_guarantor = req_guarantor_input == 'y'
                    
                    app = PersonalCredit(app_id, customer, amount=amount, months=months, tea=tea, requires_guarantor=requires_guarantor)
                    self._manager.add_application(app)
                    print(f"Credit Application created successfully with ID: {app_id}")
                elif choice == '4':
                    app_id = self._get_string_input("Enter Application ID (e.g. APP-100): ")
                    self._manager.evaluate_application(app_id)
                elif choice == '5':
                    customer = self._select_customer()
                    if not customer:
                        continue
                    self._manager.list_applications_by_customer_and_status(customer.person_id, "APPROVED")
                elif choice == '6':
                    customer = self._select_customer()
                    if not customer:
                        continue
                    self._manager.list_applications_by_customer_and_unapproved(customer.person_id)
                elif choice == '7':
                    print("Exiting system. Goodbye!")
                    break
                else:
                    print("Invalid option, try again.")
            except InvalidDataException as e:
                print(f"VALIDATION ERROR: {e.message}")
            except Exception as e:
                print(f"SYSTEM ERROR: {e}")
