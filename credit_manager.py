from typing import List, Optional
from customer import Customer
from credit_application import CreditApplication

class CreditManager:
    """Controller class managing central lists and business logic."""
    def __init__(self):
        self._customers: List[Customer] = []
        self._applications: List[CreditApplication] = []

    def add_customer(self, customer: Customer):
        self._customers.append(customer)
        print(f"Customer {customer.name} registered successfully.")

    def add_application(self, application: CreditApplication):
        self._applications.append(application)
        print(f"Application {application.application_id} registered successfully.")

    def evaluate_application(self, app_id: str):
        for app in self._applications:
            if app.application_id == app_id:
                if app.status != "PENDING":
                    print("Application already evaluated.")
                    return
                is_approved = app.evaluate_risk()
                print(f"Evaluation finished. Status: {app.status}")
                return
        print("Application not found.")

    def list_applications_by_status(self, status: str):
        filtered = [app for app in self._applications if app.status == status.upper()]
        if not filtered:
            print(f"No applications found with status: {status.upper()}")
        for app in filtered:
            app.show_summary()

    def get_first_customer(self) -> Optional[Customer]:
        return self._customers[0] if self._customers else None
