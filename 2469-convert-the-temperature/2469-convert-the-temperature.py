class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = 0.0
        fahrenheit = 0.0
        op = []
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        op.append(kelvin)
        op.append(fahrenheit)
        return op