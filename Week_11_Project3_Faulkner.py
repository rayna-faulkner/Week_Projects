from breezypythongui import EasyFrame


class TemperatureConverter(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title="Temperature Converter")

        self.addLabel(text="Celsius", row=0, column=0)
        self.celsiusField = self.addFloatField(value=0.0, row=1, column=0, precision=2)

        self.addLabel(text="Fahrenheit", row=0, column=1)
        self.fahrenheitField = self.addFloatField(value=32.0, row=1, column=1, precision=2)

        self.addButton(text=">>>>", row=2, column=0, command=self.convertToFahrenheit)
        self.addButton(text="<<<<",  row=2, column=1, command=self.convertToCelsius)

    def convertToFahrenheit(self, optional=None):
        Celsius = self.celsiusField.getNumber()
        Fahrenheit = Celsius * 9 / 5 + 32
        self.fahrenheitField.setNumber(Fahrenheit)

    def convertToCelsius(self, event=None):
        Fahrenheit = self.fahrenheitField.getNumber()
        Celsius = (Fahrenheit - 32) * 5 / 9
        self.celsiusField.setNumber(Celsius)

def main():
    TemperatureConverter().mainloop()

if __name__ == "__main__":
    main()
