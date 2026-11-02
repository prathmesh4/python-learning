import csv
import random
import sys
import os

#Generate CSV file
filename="sales.csv"

with open(filename , "w",newline="" )as file:
    writer= csv.writer(file)
    writer.writerow(["id","product","amount","quantity"])
    for i in range(10000):
        writer.writerow([
            i+1,
            f"Product_{random.randint(1,20)}",
            random.randint(100,1000),
            random.randint(1,10)
        ])
print("CSV file Generated successfully!!!")        
#Read file Lazily
def read_lines(filename):
    with open(filename, "r") as file:
        next(file)

        for line in file:
            yield line.strip()
#parse CSV file            
def parse_rows(lines):
    for line in lines:
        row = next(csv.reader([line]))
        yield{
            "id":row[0],
            "product":row[1],
            "amount":int(row[2]),
            "quantity":int(row[3])
        } 
#filter rows
def filter_rows(rows):
    for row in rows:
        if row["amount"] >= 500:
            yield row
#transform rows
def transform_rows(rows):
    for row in rows:
        yield{
        "id":row["id"],
        "product":row["product"],
        "amount": row["amount"],
        "total":row["amount"] * row["quantity"]
    }                    
#aggregate results
def aggregate(rows):
    count=0
    total_amount=0
    for row in rows:
        count +=1
        total_amount +=row["amount"]
    return count,total_amount
#build generator pipeline
lines=read_lines(filename)   
parsed=parse_rows(lines)
filtered=filter_rows(parsed)
transformed=transform_rows(filtered)             
macthin_count,amount_sum=aggregate(transformed)
#display result
print("------- Pipeline Results -------")
print("Rows processed:", 10000)
print("Machting rows:",macthin_count)
print("Sum of amount column:",amount_sum)
#Generator approch - Memoery comparison
generator=read_lines(filename)
with open(filename,"r") as file:
    next(file)
    data_list=list(file)
print("---- Memory Comparison ----")    
print("Generator object size:", sys.getsizeof(generator),"bytes")
print("List object size:", sys.getsizeof(data_list),"bytes")
print("List + string objects:", sys.getsizeof(data_list) + sum(sys.getsizeof(item) for item in data_list),"bytes")
#cleanup
os.remove(filename)
"""Generator Data Pipeline
Generators and memory efficiency
Generate a CSV file with 10,000+ rows. Build a pipeline of generators that processes it lazily, one row at a time:
read lines -> parse -> filter -> transform -> aggregate.

Then show that the generator approach uses far less memory than loading the whole file into a list (compare with sys.getsizeof, or explain the difference in a note).

Example:

Rows processed: 10000
Matching rows: 3172
Sum of 'amount' column: 1580342
Memory: generator ~ constant, list ~ grows with t
"""