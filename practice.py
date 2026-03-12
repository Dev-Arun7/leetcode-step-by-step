def my_function(words):
    result = sorted(words, key=lambda word: word.lower())
    return result





example_words = ["Zebra", "apple", "Mango", "banana", "kiwi"]
result = my_function(example_words)
print(result)