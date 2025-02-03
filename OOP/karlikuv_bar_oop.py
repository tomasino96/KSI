class Product():
    def __init__(self, name: str, price: float, stock: int) -> None:
        self.name = name
        self.price = price
        self.stock = stock
    
    def sell(self, amount: int) -> bool:
        if amount > self.stock:
            return False
        self.stock -= amount
        return True
    
    def change_price(self, percentage: int) -> None:
        self.price *= percentage / 100
    
    def restock(self, amount: int) -> None:
        self.stock += amount
     
     
class Drink(Product):
    def __init__(self, name: str, price: int, 
                 stock: int, alcoholic: bool) -> None:
        super().__init__(name, price, stock)
        self.alcoholic = alcoholic
    
    def is_alcoholic(self) -> str:
        if self.alcoholic:
            return "Obsahuje alkohol"
        return "Neobsahuje alkohol"