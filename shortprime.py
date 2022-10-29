def check_short_prime(number, steps):
    if len(number) == 1:
        return steps
    mult = 1
    for digit in number:
        mult *= int(digit)

    steps += 1
    steps = check_short_prime(str(mult), steps)
    return steps

print("Hello, World!")
number = input("Enter a number to check - ")
print(f"It took {check_short_prime(number, 0)} steps to reach single digit.")
