import re
from collections import Counter

def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    return len(text.replace(" ", ""))

def get_sentence_count(text):
    sentences = re.split(r"[.!?]+", text.strip())
    return len([sentence for sentence in sentences if sentence.strip()])

def get_avg_word_length(text):
    words = text.split()

    if not words:
        return 0.0

    total_length = sum(len(word.strip(".,!?;:\"'()")) for word in words)
    return round(total_length / len(words), 1)

def get_most_common_word(text):
    words = re.findall(r"\b\w+\b", text.lower())

    if not words:
        return ""

    return Counter(words).most_common(1)[0][0]

def get_longest_word(text):
    words = re.findall(r"\b\w+\b", text)

    if not words:
        return ""

    return max(words, key=len)

def analyze(text):
    return {
        "word_count": get_word_count(text),
        "char_count": get_char_count(text),
        "sentence_count": get_sentence_count(text),
        "avg_word_length": get_avg_word_length(text),
        "most_common_word": get_most_common_word(text),
        "longest_word": get_longest_word(text),
    }

text = input("Enter some text: ")
result = analyze(text)
print("\n===== TEXT ANALYSIS =====")
for statistic, value in result.items():
    print(f"{statistic}: {value}")