class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        print(f"Disconnecting {self.name}")
        self.connected = False
        print("Disconnected.")


printer = Device('Office Printer', 'USB')
print(printer)
printer.disconnect()


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print(f"{self.name} is not connected!")
            return
        if self.remaining_pages < pages:
            print(f"printing {self.remaining_pages} pages")
            self.remaining_pages = 0
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


printer = Printer('Office Printer', 'USB', 500)
printer.print(20)
print(printer)
printer.disconnect()
printer.print(340)
