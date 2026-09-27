import uuid
from controllers.credit_manager import CreditManager
from models.individual_customer import IndividualCustomer
from models.corporate_customer import CorporateCustomer
from models.analyst import Analyst
from models.personal_credit import PersonalCredit
from models.vehicle_credit import VehicleCredit
from models.mortgage_credit import MortgageCredit
from exceptions.invalid_data_exception import InvalidDataException

class ConsoleMenu:
    """Handles CLI User Interface."""
    def __init__(self):
        self._manager = CreditManager()
        a1 = Analyst(f"A-{uuid.uuid4().hex[:6].upper()}", "Ana Torres", "ana@bank.com", "999111222", "EMP01", 10000.0)
        a2 = Analyst(f"A-{uuid.uuid4().hex[:6].upper()}", "Carlos Ruiz", "carlos@bank.com", "999333444", "EMP02", 500000.0)
        self._manager.add_analyst(a1)
        self._manager.add_analyst(a2)

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
            print("2. Register Analyst")
            print("3. List Customers")
            print("4. List Analysts")
            print("5. Create Credit App")
            print("6. Evaluate Application")
            print("7. List Approved Applications")
            print("8. List Unapproved Applications")
            print("9. Exit")
            choice = input("Select an option: ").strip()

            try:
                if choice == '1':
                    print("\n--- Register Customer ---")
                    print("1. Individual Customer")
                    print("2. Corporate Customer")
                    cust_type = self._get_string_input("Select customer type: ")
                    
                    person_id = f"C-{uuid.uuid4().hex[:6].upper()}"
                    name = self._get_string_input("Enter Contact Name: ")
                    email = self._get_string_input("Enter Email: ")
                    phone = self._get_string_input("Enter Phone: ")
                    monthly_income = self._get_float_input("Enter Monthly Income: ")
                    
                    if cust_type == '1':
                        dni = self._get_string_input("Enter DNI (8 digits): ")
                        workplace = self._get_string_input("Enter Workplace: ")
                        cust = IndividualCustomer(person_id, name, email, phone, monthly_income, dni, workplace)
                    elif cust_type == '2':
                        ruc = self._get_string_input("Enter RUC (11 digits): ")
                        company_name = self._get_string_input("Enter Company Name: ")
                        years = self._get_int_input("Enter Years in Operation: ")
                        cust = CorporateCustomer(person_id, name, email, phone, monthly_income, ruc, company_name, years)
                    else:
                        print("Invalid customer type. Registration cancelled.")
                        continue
                        
                    self._manager.add_customer(cust)
                    print(f"Customer registered successfully with ID: {person_id}")
                elif choice == '2':
                    print("\n--- Register Analyst ---")
                    person_id = f"A-{uuid.uuid4().hex[:6].upper()}"
                    name = self._get_string_input("Enter Analyst Name: ")
                    email = self._get_string_input("Enter Email: ")
                    phone = self._get_string_input("Enter Phone: ")
                    emp_code = self._get_string_input("Enter Employee Code: ")
                    limit = self._get_float_input("Enter Approval Limit ($): ")
                    analyst = Analyst(person_id, name, email, phone, emp_code, limit)
                    self._manager.add_analyst(analyst)
                    
                elif choice == '3':
                    print("\n--- List Customers ---")
                    customers = self._manager.get_customers()
                    if not customers:
                        print("No customers registered.")
                    else:
                        for cust in customers:
                            print(f"- {cust.name} | ID: {cust.person_id} | Income: {cust.monthly_income}")
                            
                elif choice == '4':
                    print("\n--- List Analysts ---")
                    analysts = self._manager.get_analysts()
                    if not analysts:
                        print("No analysts registered.")
                    else:
                        for an in analysts:
                            print(f"- {an.name} | ID: {an.person_id} | Limit: ${an._approval_limit}")
                            
                elif choice == '5':
                    customer = self._select_customer()
                    if not customer:
                        continue
                        
                    print("\n--- Create Credit App ---")
                    print("1. Personal Credit")
                    print("2. Vehicle Credit")
                    print("3. Mortgage Credit")
                    cred_type = self._get_string_input("Select credit type: ")
                    
                    if cred_type not in ['1', '2', '3']:
                        print("Invalid credit type. Application cancelled.")
                        continue
                        
                    print(f"Creating app for customer: {customer.name}")
                    app_id = f"APP-{uuid.uuid4().hex[:6].upper()}"
                    amount = self._get_float_input("Enter Amount: ")
                    months = self._get_int_input("Enter Months: ")
                    tea = self._get_float_input("Enter TEA (e.g. 0.15 for 15%): ")
                    
                    if cred_type == '1':
                        req_guarantor_input = self._get_string_input("Requires guarantor? (y/n): ").lower()
                        requires_guarantor = req_guarantor_input == 'y'
                        app = PersonalCredit(app_id, customer, amount=amount, months=months, tea=tea, requires_guarantor=requires_guarantor)
                    elif cred_type == '2':
                        down_payment = self._get_float_input("Enter Down Payment: ")
                        app = VehicleCredit(app_id, customer, amount=amount, months=months, tea=tea, down_payment=down_payment)
                    elif cred_type == '3':
                        property_value = self._get_float_input("Enter Property Value: ")
                        app = MortgageCredit(app_id, customer, amount=amount, months=months, tea=tea, property_value=property_value)
                        
                    self._manager.add_application(app)
                    print(f"Credit Application created successfully with ID: {app_id}")
                elif choice == '6':
                    app_id = self._get_string_input("Enter Application ID (e.g. APP-100): ")
                    analysts = self._manager.get_analysts()
                    if not analysts:
                        print("Please register an analyst first.")
                        continue
                        
                    print("\n--- Select Analyst ---")
                    for i, an in enumerate(analysts, 1):
                        print(f"{i}. {an.name} (Limit: ${an._approval_limit}) - ID: {an.person_id}")
                    an_idx = self._get_int_input("Select analyst number (0 to cancel): ")
                    if an_idx == 0:
                        continue
                    if 1 <= an_idx <= len(analysts):
                        analyst_id = analysts[an_idx - 1].person_id
                        self._manager.evaluate_application(app_id, analyst_id)
                    else:
                        print("Invalid selection.")
                        
                elif choice == '7':
                    customer = self._select_customer()
                    if not customer:
                        continue
                    self._manager.list_applications_by_customer_and_status(customer.person_id, "APPROVED")
                elif choice == '8':
                    customer = self._select_customer()
                    if not customer:
                        continue
                    self._manager.list_applications_by_customer_and_unapproved(customer.person_id)
                elif choice == '9':
                    print("Exiting system. Goodbye!")
                    break
                else:
                    print("Invalid option, try again.")
            except InvalidDataException as e:
                print(f"VALIDATION ERROR: {e.message}")
            except Exception as e:
                print(f"SYSTEM ERROR: {e}")
