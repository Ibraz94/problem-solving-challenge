

def sum_of_digits_modulus(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10
    return total

def sum_of_digits_string(num):

    return sum(int(digit) for digit in str(num))

if __name__ == "__main__":
    test_cases = [12345, 0, 999, 1000, 5]
    
    print("Sum of Digits (String Method):")
    for num in test_cases:
        result = sum_of_digits_string(num)
        print(f"Input: {num}, Output: {result}")
    
    print("\nSum of Digits (Modulus Method):")
    for num in test_cases:
        result = sum_of_digits_modulus(num)
        print(f"Input: {num}, Output: {result}")

