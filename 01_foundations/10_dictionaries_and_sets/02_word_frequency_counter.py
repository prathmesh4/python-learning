import string

text=input("Enter a paragraph : ").lower()

for punctuation in string.punctuation:
    text=text.replace(punctuation, "")
    
words=text.split()    
frequency={}

for w in words:
    if w in frequency:
        frequency[w] +=1
    else:
        frequency[w]=1    

sorted_words= sorted(frequency.items(),key=lambda item: item[1],reverse=True)

print("Word frequencies:")        
for word, count in sorted_words:
    print(f"{word} : {count}")
    
print("Unique words: ", len(frequency))    

if frequency:
    most_common=sorted_words[0]
    least_count  =sorted_words[-1][1]
    
    least_common=[
        (word,count)
        for word,count in sorted_words
        if count==least_count
    ]
    
    print(f"Most common: {most_common[0]} ({most_common[1]})")
    print("Least common: ", end="")
    print(", ".join(f"{word} ({count})" for word ,count in least_common))
else:
    print("No word found.")    

"""Word Frequency Counter
Counting with dictionaries, case-insensitive
Given a paragraph of text, count how often each word appears (case-insensitive, and ignore punctuation). Then report:
• Each word with its count, sorted by frequency (highest first)
• The total number of unique words
• The most common and least common word

Example:

Text: "The cat sat. The dog ran. The cat slept."

the: 3
cat: 2
sat: 1
dog: 1
ran: 1
slept: 1
Unique words: 6
Most common: the (3)
"""    