raw = [
    "Ana,23,88",
    "Ben,19,45",
    "Cara,31,72",
    "prathmenh,30,89",
    "dilip,sds,87",
    "pranav,27,88"
]
parsed=[
    dict(zip(["name","age","score"],row.split(",")))
    for row in raw
]
valid=[
    {**r,"age": int(r["age"]),"score":int(r["score"])}
    for r in parsed
    if r["age"].isdigit()
    and r["score"].isdigit()
    and int(r["score"])>=60
]
sorted_data=sorted(valid,key=lambda r: r["score"],reverse=True)
formatted=[f'{r["name"]} : {r["score"]}' for r in sorted_data]
average = round(
    sum(r["score"] for r in sorted_data) / len(sorted_data), 2
) if sorted_data else 0

print("Parsed:", len(parsed), "records")
print("Filtered:", [r["name"] for r in valid])
print("Sorted:", [f'{r["name"]}({r["score"]})' for r in sorted_data])
print("Formatted:", formatted)
print("Average score:", average)

"""Data Pipeline
Chaining comprehension steps into a pipeline
Given raw CSV-like strings (rows such as "name,age,score"), build a pipeline where each stage is a one-liner comprehension:
1. parse each row into a dict
2. filter out invalid or low-scoring rows
3. sort by a field
4. format each record into a display string
5. aggregate a summary statistic

Example:

raw = ["Ana,23,88", "Ben,19,45", "Cara,31,72"]

Parsed          -> 3 records
Filter score>=60 -> Ana, Cara
Sorted by score -> Ana(88), Cara(72)
Formatted       -> ["Ana: 88", "Cara: 72"]
Average score: 80.0
"""