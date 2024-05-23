# Python Script - convert Categories CSV into Django JSON Fixtures format

import json
import csv

data_array = []
with open('categories.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)  # skip the headers

    for row in csvreader:
        print(row)
        pk = int(row[0])
        name = row[1]
        friendly_name = row[2]
        group = row[3]

        jsonObj = {
            "pk": pk,
            "model": "products.category",
            "fields": {
                "name": name,
                "friendly_name": friendly_name,
                "group": group
            }
        }

        data_array.append(jsonObj)

    print(json.dumps(data_array))
    with open('categories.json', 'w', encoding='utf-8') as f:
        json.dump(data_array, f, ensure_ascii=False, indent=4)