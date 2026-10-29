numbers=[]
for i in range(5):
    num=int(input("Enter number : "))
    numbers.append(num)

sorted_numbers=numbers.copy()
for i in range(len(sorted_numbers)):
    for j in range(i+1,len(sorted_numbers)):
        if sorted_numbers[i]> sorted_numbers[j]:
            temp=sorted_numbers[i]
            sorted_numbers[i]=sorted_numbers[j]
            sorted_numbers[j]=temp
                
reversed_numbers=numbers[::-1]

total=0
minimum=numbers[0]
maximum=numbers[0]

for num in numbers:
    total +=num
    
    if num>maximum:
        maximum=num
        
    if num<minimum:
        minimum=num
            
average=total/len(numbers)            
print("Numbers:", numbers)
print("Sorted:", sorted_numbers)
print("Reversed:", reversed_numbers)
print("Sum:", total)
print("Average:", average)
print("Max:", maximum, "Min:", minimum)


"""Manual Statistics
Looping over a list to compute stats by hand
Read 5 numbers into a list. WITHOUT using the built-in sum(), min(), or max(), compute and print:
• the list sorted in ascending order
• the list reversed
• the sum
• the average
• the maximum and the minimum

Example:

Numbers: [42, 17, 8, 99, 23]
Sorted: [8, 17, 23, 42, 99]
Reversed: [23, 99, 8, 17, 42]
Sum: 189
Average: 37.8
Max: 99, Min: 8

Compute the sum, max, and min yourself with a loop — that's the learning goal here.
"""