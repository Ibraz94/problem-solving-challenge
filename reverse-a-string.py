def reverse_string(s):

    return s[::-1]

if __name__ == "__main__":
    
    test_string = "hello"
    reversed_string = reverse_string(test_string)
    print(f"Input: {test_string}")
    print(f"Output: {reversed_string}")
