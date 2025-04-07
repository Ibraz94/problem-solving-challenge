def count_vowels(text):
    text = text.lower()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = sum(1 for char in text if char in vowels)
    
    return count


if __name__ == "__main__":

    test_string = "Apple"
    result = count_vowels(test_string)
    print(f"Input: {test_string}")
    print(f"Output: {result}")
