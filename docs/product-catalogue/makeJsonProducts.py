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
        if row[5] == '':
            description = None
        else:
            description = row[5]
        if row[6] == '':
            image = None
        else:
            image = row[6]
        if row[7] == '':
            alt_text = None
        else:
            alt_text = row[7]
        if row[8] == '':
            bs_icon = None
        else:
            bs_icon = row[8]
        if row[9] == '':
            organic = None
        else:
            organic = row[9]
        if row[10] == '':
            weight = None
        else:
            weight = int(row[10])
        if row[11] == '':
            strength = None
        else:
            strength = int(row[11])
        if row[12] == '':
            brew_time = None
        else:
            brew_time = row[12]
        if row[13] == '':
            water_temp = None
        else:
            water_temp = int(row[13])
        if row[14] == '':
            price = None
        else:
            price = float(row[14])
        if row[15] == '':
            stock_level = None
        else:
            stock_level = int(row[15])
        if row[16] == '':
            rating = None
        else:
            rating = float(row[16])

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
                "organic": organic,
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
