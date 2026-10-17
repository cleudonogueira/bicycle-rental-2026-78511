from rental_item import RentalItem

class Bicycle(RentalItem):
    def __init__(self, item_id: str, model: str, hourly_rate: float, is_rented: bool = False):
        super().__init__(item_id, is_rented)
        
        if hourly_rate <= 0:
            raise ValueError("Hourly rate must be greater than zero.")
            
        self.model = model
        self.hourly_rate = hourly_rate

    def borrow_item(self) -> bool:
        if self.is_rented:
            print(f"Bicycle {self.model} is already rented.")
            return False
        self.is_rented = True
        print(f"Bicycle {self.model} successfully rented.")
        return True

    def return_item(self) -> bool:
        if not self.is_rented:
            print(f"Bicycle {self.model} was not rented.")
            return False
        self.is_rented = False
        print(f"Bicycle {self.model} successfully returned.")
        return True

    def calculate_rental_cost(self, hours: float) -> float:
        if hours <= 0:
            raise ValueError("Rental hours must be greater than zero.")
        return self.hourly_rate * hours

    @classmethod
    def from_string(cls, data_str: str):
        parts = data_str.split(",")
        return cls(parts[0].strip(), parts[1].strip(), float(parts[2]))

    def __str__(self):
        status = "Rented" if self.is_rented else "Available"
        return f"[{self.item_id}] {self.model} - €{self.hourly_rate}/h [{status}]"