from abc import ABC, abstractmethod

class OrderCalculator(ABC):
    @abstractmethod
    def calculate_total(self, order_d):
        pass

class SumCalculator(OrderCalculator):
    def calculate_total(self, order_d):
        return sum(order_d)

class DiscountCalculator(OrderCalculator):
    def __init__(self, discount):
        self.discount = discount

    def calculate_total(self, order_d):
        total = sum(order_d)
        dis = total * (self.discount / 100)
        return total - dis

class LateChargeCalculator(OrderCalculator):
    def __init__(self, late, days_late):
        self.late = late
        self.days_late = days_late

    def calculate_total(self, order_details):
        total = sum(order_details)
        late_charge = total * (self.late / 100) * self.days_late
        return total + late_charge

class OrderContainer:
    def __init__(self):
        self.o = []

    def __getitem__(self, index):
        return self.o[index]

    def __setitem__(self, index, value):
        self.o[index] = value

    def __iter__(self):
        return iter(self.o)

    def add_order(self, order_calculator, order_details):
        self.o.append((order_calculator, order_details))


order_c = OrderContainer()

order_c.add_order(SumCalculator(), [10, 20, 30])
order_c.add_order(DiscountCalculator(10), [50, 75, 25])
order_c.add_order(LateChargeCalculator(5, 3), [100, 200])

for i in order_c:
    print(i.calculate_total())