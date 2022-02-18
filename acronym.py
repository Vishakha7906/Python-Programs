import re
def abbreviate(words):
    cleaned = re.sub(r'[^a-zA-Z\s\']', ' ', words)
    return ''.join([word[0] for word in cleaned.split()]).upper()
