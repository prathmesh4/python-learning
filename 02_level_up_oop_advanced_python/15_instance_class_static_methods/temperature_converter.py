class Temperature:
    def __init__(self,celsius):
        self._celsius = celsius
    @classmethod
    def from_fahrenheit(cls,f):
        celsius=cls.fahrenheit_to_celsius(f)
        return cls(celsius)
    @classmethod
    def from_kelvin(cls,k):
            celsius=cls.kelvin_to_celsius(k)
            return cls(celsius)    
    def to_fahrenheit(self):
        return self.celsius_to_fahrenheit(self._celsius)
    def to_kelvin(self):
            return self.celsius_to_kelvin(self._celsius)
    def dsiplay(self):
        print(
            f"{self._celsius:.2f}'C |"
            f"{self.to_fahrenheit():.2f}'f |"
            f"{self.to_kelvin():.2f}K |"
        )        
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c *9 /5 ) +32
    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) *5/9   
    @staticmethod
    def celsius_to_kelvin(c):
        return c  + 273.15   
    @staticmethod
    def kelvin_to_celsius(k):
        return k - 273.15
    @staticmethod
    def is_valid_celsius(c):
        return c  >= -273.15   
        
boiling=Temperature(100)
body=Temperature.from_fahrenheit(98.6)
absolute_zero=Temperature.from_kelvin(0)
print("water boiling point: ")        
boiling.dsiplay()
print("Body temperature (created from 98.6 'F):")
body.dsiplay()
print("Absolute zero (created from 0K):")
absolute_zero.dsiplay()
print("Static conversions:")
print(
    f"25°C = "
    f"{Temperature.celsius_to_fahrenheit(25):.2f}°F"
)
print(
    f"77°F = "
    f"{Temperature.fahrenheit_to_celsius(77):.2f}°C"
)
print(
    f"25°C = "
    f"{Temperature.celsius_to_kelvin(25):.2f}K"
)
print(
    f"300K = "
    f"{Temperature.kelvin_to_celsius(300):.2f}°C"
)
print(
    f"is_valid_celsius(25): "
    f"{Temperature.is_valid_celsius(25)}"
)
print(
    f"is_valid_celsius(-300): "
    f"{Temperature.is_valid_celsius(-300)}"
)
print(
    f"is_valid_celsius(-273.15): "
    f"{Temperature.is_valid_celsius(-273.15)}"
)