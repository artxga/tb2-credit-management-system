import uuid
from credit_manager import CreditManager
from individual_customer import IndividualCustomer
from personal_credit import PersonalCredit
from invalid_data_exception import InvalidDataException

class ConsoleMenu:
    """Handles CLI User Interface."""
    def __init__(self):
        self._manager = CreditManager()

    def _select_customer(self):
        customers = self._manager.get_customers()
        if not customers:
            print("Please register a customer first.")
            return None
            
        print("\n--- Select Customer ---")
        for i, cust in enumerate(customers, 1):
            print(f"{i}. {cust.name} (ID: {cust.person_id})")
        
        try:
            cust_idx = int(input("Select customer number: ")) - 1
            if cust_idx < 0 or cust_idx >= len(customers):
                print("Invalid selection.")
                return None
            return customers[cust_idx]
        except ValueError:
            print("Invalid input.")
            return None

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
            choice = input("Select an option: ")

            try:
                if choice == '1':
                    print("\n--- Register Customer ---")
                    person_id = f"C-{uuid.uuid4().hex[:6].upper()}"
                    name = input("Enter Name: ")
                    email = input("Enter Email: ")
                    phone = input("Enter Phone: ")
                    monthly_income = float(input("Enter Monthly Income: "))
                    dni = input("Enter DNI (8 digits): ")
                    workplace = input("Enter Workplace: ")
                    
                    cust = IndividualCustomer(person_id, name, email, phone, monthly_income, dni, workplace)
                    self._manager.add_customer(cust)
                    print(f"Customer registered successfully with ID: {person_id}")
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
                    amount = float(input("Enter Amount: "))
                    months = int(input("Enter Months: "))
                    tea = float(input("Enter TEA (e.g. 0.15 for 15%): "))
                    req_guarantor_input = input("Requires guarantor? (y/n): ").strip().lower()
                    requires_guarantor = req_guarantor_input == 'y'
                    
                    app = PersonalCredit(app_id, customer, amount=amount, months=months, tea=tea, requires_guarantor=requires_guarantor)
                    self._manager.add_application(app)
                    print(f"Credit Application created successfully with ID: {app_id}")
                elif choice == '4':
                    app_id = input("Enter Application ID (e.g. APP-100): ")
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
