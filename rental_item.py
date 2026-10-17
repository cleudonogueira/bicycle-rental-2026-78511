from abc import ABC, abstractmethod

class RentalItem(ABC):
    def __init__(self, item_id, is_rented=False):
        self.item_id = item_id
        self.is_rented = is_rented

    @abstractmethod
    def borrow_item(self):
        pass

    @abstractmethod
    def return_item(self):
        pass

    @abstractmethod
    def calculate_rental_cost(self, hours):
        pass