# Statement-: Determine if a word or phrase is an isogram.
#Program-:
def check_isogram(str1): # An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.
    return len(str1) == len(set(str1.lower()))

print(check_isogram("lumberjacks"))
print(check_isogram("background"))
print(check_isogram("programmer"))
print(check_isogram("Java"))
)
