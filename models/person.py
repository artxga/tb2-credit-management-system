from abc import ABC, abstractmethod

class Person(ABC):
    """Abstract base class for all persons."""
    def __init__(self, person_id: str, name: str, email: str, phone: str):
        self._person_id = person_id
        self._name = name
        self._email = email
        self._phone = phone

    @property
    def person_id(self) -> str: return self._person_id
    
    @property
    def name(self) -> str: return self._name

    @abstractmethod
    def show_details(self) -> str:
        pass
