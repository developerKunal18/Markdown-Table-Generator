rows = []

print("Enter rows of data separated by commas.")
print("Type 'done' when finished.\n")

while True:
    row = input("Enter row: ")
    if row.lower() == "done":
        break
    rows.append(row.split(","))

if rows:
    headers = rows[0]

    print("\nMarkdown Table:\n")

    print("| " + " | ".join(headers) + " |")
    print("|" + "|".join(["---"] * len(headers)) + "|")

    for row in rows[1:]:
        print("| " + " | ".join(row) + " |")
else:
    print("No data entered.")
