class Value:
    def __init__(self, value):
        self._value = value  # Use a different variable name for internal storage

    @property
    def value(self):
        return self._value  # Return the internal variable

    @value.setter
    def value(self, value):
        self._value = value  # Set the internal variable
