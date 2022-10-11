import csv

# open("data.csv", "w")
# file.close()

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price_id"])
    writer.writerow([100, 10, 5])
    writer.writerow([500, 40, 20])

with open("data.csv") as file:
    reader = csv.reader(file)
    # La lectura provoca que el indice quede al final del archivo
    # print(list(reader))
    for row in reader:
        print(row)
