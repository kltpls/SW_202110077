# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius_temp = 25
fahrenheit_temp = 77

print(f"{celsius_temp}°C는 {celsius_to_fahrenheit(celsius_temp):.2f}°F입니다.")
print(f"{fahrenheit_temp}°F는 {fahrenheit_to_celsius(fahrenheit_temp):.2f}°C입니다.")







def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

meters_length = 10
feet_length = 32.8

print(f"{meters_length}미터는 {meters_to_feet(meters_length):.2f}피트입니다.")
print(f"{feet_length}피트는 {feet_to_meters(feet_length):.2f}미터입니다.")





