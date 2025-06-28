def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

# Example:
print(is_anagram("listen", "silent"))  # True
