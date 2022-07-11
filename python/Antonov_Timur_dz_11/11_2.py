class DivisionNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Делить на ноль нельзя")


div = DivisionNull(10, 100)
print(DivisionNull.divide_by_null(10, 0))
print(DivisionNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))
