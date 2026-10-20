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