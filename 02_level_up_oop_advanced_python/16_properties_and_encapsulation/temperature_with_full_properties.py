class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self, value):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError("Temperature must be a number")
        if value < -273.15:
            raise ValueError(
                "Temperature cannot be below absolute zero (-273.15°C)"
            )
        self._celsius = value
    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9
    @property
    def kelvin(self):
        return self._celsius + 273.15
    @kelvin.setter
    def kelvin(self, value):
        self.celsius = value - 273.15
    @property
    def state(self):
        if self._celsius < 0:
            return "solid"
        elif self._celsius <= 100:
            return "liquid"
        elif self._celsius > 10000:
            return "plasma"
        else:
            return "gas"
    def __str__(self):
        return (
            f"Temperature: {self.celsius:.2f}°C | "
            f"{self.fahrenheit:.2f}°F | "
            f"{self.kelvin:.2f}K | "
            f"State: {self.state}"
        )

temp = Temperature(100)
print(temp)
print("Setting fahrenheit to 32...")
temp.fahrenheit = 32
print(temp)
print("Setting kelvin to 0...")
temp.kelvin = 0
print(temp)
print("Setting celsius to -300...")
try:
    temp.celsius = -300
except ValueError as e:
    print(f"Error: {e}")
print("Setting celsius to 15000...")
temp.celsius = 15000
print(f"State: {temp.state}")