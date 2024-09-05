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




total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number

print("짝수의 합:", total)





even_sum = sum([number for number in range(1, 101) if number % 2 == 0])

print("짝수의 합:", even_sum)





a = 2
l = 100
n = (l - a) // 2 + 1
even_sum = n * (a + l) // 2

print("짝수의 합:", even_sum)





even_sum = sum(range(2, 101, 2))

print("짝수의 합:", even_sum)
