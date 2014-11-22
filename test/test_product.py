import os
import json

filePath = os.path.join(os.path.dirname(__file__))
f = open("%s/../model/products.json"%filePath, "rb")
productJson = f.read()
f.close()

productList = json.loads(productJson)

productDict = dict()
for item in productList:
    itemDict = dict()
    productDict[item.get("item_id")] = itemDict
    itemDict["id"] = item.get("item_id")
    itemDict["name"] = item.get("name")
    itemDict["discount"] = item.get("discount")
    itemDict["price"] = item.get("unit_price")
    
print json.dumps(productDict)

