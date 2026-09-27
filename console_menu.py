from credit_manager import CreditManager
from individual_customer import IndividualCustomer
from personal_credit import PersonalCredit
from invalid_data_exception import InvalidDataException

class ConsoleMenu:
    """Handles CLI User Interface."""
    def __init__(self):
        self._manager = CreditManager()

    def run(self):
        while True:
            print("\n--- CREDIT MANAGEMENT SYSTEM ---")
            print("1. Register Test Customer")
            print("2. Create Personal Credit App")
            print("3. Evaluate Application")
            print("4. List Approved Applications")
            print("5. Exit")
            choice = input("Select an option: ")

            try:
                if choice == '1':
                    cust = IndividualCustomer("C001", "John Doe", "john@mail.com", "555-1234", 5000.0, "12345678", "NTT Data")
                    self._manager.add_customer(cust)
                elif choice == '2':
                    customer = self._manager.get_first_customer()
                    if not customer:
                        print("Please register a customer first.")
                        continue
                    app = PersonalCredit("APP-100", customer, amount=10000, months=12, tea=0.15, requires_guarantor=False)
                    self._manager.add_application(app)
                elif choice == '3':
                    app_id = input("Enter Application ID (e.g. APP-100): ")
                    self._manager.evaluate_application(app_id)
                elif choice == '4':
                    self._manager.list_applications_by_status("APPROVED")
                elif choice == '5':
                    print("Exiting system. Goodbye!")
                    break
                else:
                    print("Invalid option, try again.")
            except InvalidDataException as e:
                print(f"VALIDATION ERROR: {e.message}")
            except Exception as e:
                print(f"SYSTEM ERROR: {e}")
