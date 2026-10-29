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

"""Temperature with Full Properties
Interconnected properties where setting one updates the underlying state for all others
Create a Temperature class that stores temperature internally as Celsius in a private attribute _celsius.

Three properties, all with getters AND setters:
- celsius — get returns _celsius. Set validates (must be >= -273.15, absolute zero) and stores directly.
- fahrenheit — get converts from internal celsius and returns. Set converts the input from F to C and stores in _celsius.
- kelvin — get converts from internal celsius and returns. Set converts from K to C and stores in _celsius.

One read-only property:
- state — returns the state of water at the current temperature:
  - Below 0°C: "solid" (ice)
  - 0°C to 100°C: "liquid" (water)
  - Above 100°C: "gas" (steam)
  - Above 10000°C: "plasma"

Demonstrate:
1. Create at 100°C. Print all three formats and state.
2. Set fahrenheit to 32. Print celsius (should be 0). Print state (should be "solid" boundary — your choice if 0 is solid or liquid, just be consistent).
3. Set kelvin to 0. Print celsius (should be -273.15).
4. Try setting celsius to -300. Should raise ValueError (below absolute zero).
5. Set celsius to 15000. Print state (should be "plasma").

Example output:

Temperature: 100.00°C | 212.00°F | 373.15K | State: gas

Setting fahrenheit to 32...
Temperature: 0.00°C | 32.00°F | 273.15K | State: liquid

Setting kelvin to 0...
Temperature: -273.15°C | -459.67°F | 0.00K | State: solid

Setting celsius to -300...
Error: Temperature cannot be below absolute zero (-273.15°C)

Setting celsius to 15000...
State: plasma
"""