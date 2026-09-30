numbers = [12, 345, 6789, 42, 7, 1234, 56, 890]

count = 0

print("User Data:", numbers)
print("\nNumbers with even number of digits:")

for number in numbers:
    # Convert number to string and count its digits
    digit_count = len(str(abs(number)))

    if digit_count % 2 == 0:
        print(number, "->", digit_count, "digits")
        count += 1

print("\nTotal numbers with even digits:", count)