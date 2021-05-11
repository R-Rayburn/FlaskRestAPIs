class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        if name in [i.name for i in self.items]:
            [i for i in self.items if i.name == name][0].price = price
        else:
            self.items.append(Item(name, price))

    def __repr__(self):
        return f"<Store('{self.name}')>"
            
    def stock_price(self):
        return sum(item.price for item in self.items)

    def stock_list(self):
        for item in self.items:
            print(f"{item.name} for {item.price}")

    @classmethod
    def franchise(cls, store):
        return cls(store.name + " - franchise")

    @staticmethod
    def store_details(store):
        return f"{store.name}, total stock price: {store.stock_price()}"

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

store = Store("Lifeway")

store.add_item("Hardback KJV", 5.99)
store.add_item("Softback NKJV", 2.89)
print(store.stock_price())
store.stock_list()

print(Store.franchise(store))
print(Store.store_details(store))
