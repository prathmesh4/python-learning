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

"""Temperature Converter
All three method types working together — instance, class, and static in one coherent class
Create a Temperature class that stores temperature internally in Celsius.

Instance attributes:
- _celsius — the stored value (set via __init__ which takes celsius)

Class methods (alternative constructors):
- from_fahrenheit(f) — creates a Temperature from Fahrenheit. Formula: C = (F - 32) × 5/9
- from_kelvin(k) — creates a Temperature from Kelvin. Formula: C = K - 273.15

Instance methods:
- to_fahrenheit() — returns the value in Fahrenheit
- to_kelvin() — returns the value in Kelvin
- display() — prints all three formats rounded to 2 decimal places

Static methods (pure conversion utilities):
- celsius_to_fahrenheit(c) — converts and returns
- fahrenheit_to_celsius(f) — converts and returns
- celsius_to_kelvin(c) — converts and returns
- kelvin_to_celsius(k) — converts and returns
- is_valid_celsius(c) — returns True if above absolute zero (-273.15°C)

Demonstrate:
1. Create a Temperature using all three constructors (direct Celsius, from_fahrenheit, from_kelvin)
2. Display each in all three formats
3. Use static methods independently (without creating any object)
4. Test is_valid_celsius with valid and invalid temperatures

Example output:

Water boiling point:
100.00°C | 212.00°F | 373.15K

Body temperature (created from 98.6°F):
37.00°C | 98.60°F | 310.15K

Absolute zero (created from 0K):
-273.15°C | -459.67°F | 0.00K

Static conversions:
25°C = 77.00°F
77°F = 25.00°C

is_valid_celsius(25): True
is_valid_celsius(-300): False
"""