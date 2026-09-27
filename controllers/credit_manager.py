from typing import List, Optional
from models.customer import Customer
from models.credit_application import CreditApplication

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

    def list_applications_by_customer_and_status(self, customer_id: str, status: str):
        filtered = [app for app in self._applications if app.customer.person_id == customer_id and app.status == status.upper()]
        if not filtered:
            print(f"No {status.upper()} applications found for this customer.")
        for app in filtered:
            app.show_summary()

    def list_applications_by_customer_and_unapproved(self, customer_id: str):
        filtered = [app for app in self._applications if app.customer.person_id == customer_id and app.status != "APPROVED"]
        if not filtered:
            print(f"No unapproved applications found for this customer.")
        for app in filtered:
            app.show_summary()

    def get_first_customer(self) -> Optional[Customer]:
        return self._customers[0] if self._customers else None

    def get_customers(self) -> List[Customer]:
        return self._customers

    def get_customer_by_id(self, person_id: str) -> Optional[Customer]:
        for customer in self._customers:
            if customer.person_id == person_id:
                return customer
        return None
