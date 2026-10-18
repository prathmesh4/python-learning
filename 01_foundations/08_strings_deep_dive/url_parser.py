url = input("Enter a URL: ").strip()
protocol, remainder = url.split("://", 1)
parts = remainder.split("/", 1)
domain = parts[0]

if len(parts) > 1:
    path_and_query = "/" + parts[1]
else:
    path_and_query = ""

path_parts = path_and_query.split("?", 1)
path = path_parts[0]

if len(path_parts) > 1:
    query_string = path_parts[1]
else:
    query_string = ""

print("\nProtocol:", protocol)
print("Domain:", domain)
print("Path:", path)

print("Query:")
if query_string:
    parameters = query_string.split("&")

    for parameter in parameters:
        key_value = parameter.split("=", 1)

        key = key_value[0]
        value = key_value[1] if len(key_value) > 1 else ""

        print(f"  {key} = {value}")