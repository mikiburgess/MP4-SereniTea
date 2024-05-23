# Python Script - convert Products CSV into Django JSON Fixtures format

import json
import csv

data_array = []
with open("products.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)  # skip the headers

    for row in csvreader:
        print(row)
        pk = int(row[0])
        category = int(row[1])
        sku = row[2]
        name = row[3]
        friendly_name = row[4]
        description = row[5]
        image = row[6]
        alt_text = row[7]
        bs_icon = row[8]

        if row[9] == '':
            weight = None
        else:
            weight = int(row[9])

        if row[10] == '':
            strength = None
        else:
            strength = int(row[10])

        if row[10] == '':
            brew_time = None
        else:
            brew_time = row[11]

        if row[12] == '':
            water_temp = None
        else:
            water_temp = int(row[12])

        if row[13] == '':
            price = None
        else:
            price = float(row[13])

        if row[14] == '':
            stock_level = None
        else:
            stock_level = int(row[14])
        if row[15] == '':
            rating = None
        else:
            rating = float(row[15])

        jsonObj = {
            "pk": pk,
            "model": "products.product",
            "fields": {
                "category": category,
                "sku": sku,
                "name": name,
                "friendly_name": friendly_name,
                "description": description,
                "image": image,
                "alt_text": alt_text,
                "bs_icon": bs_icon,
                "weight": weight,
                "strength": strength,
                "brew_time": brew_time,
                "water_temp": water_temp,
                "price": price,
                "stock_level": stock_level,
                "rating": rating
            }
        }

        data_array.append(jsonObj)

    print(json.dumps(data_array))
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(data_array, f, ensure_ascii=False, indent=4)
