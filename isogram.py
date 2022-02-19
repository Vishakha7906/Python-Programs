import string
def is_isogram(text):
#isogram-:An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.
    seen = set()
    for char in text:
        if (lower := char.lower()) in string.ascii_lowercase:
            if lower in seen:
                return False
            else: 
                seen.add(lower)
    return TrueLOWER_BOUND, ASCII_UPPER_BOUND + 1)
    )