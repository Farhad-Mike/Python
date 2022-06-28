import json

jsonObj = json.dumps([1, 2, 3, "a", "b", "c"])  # Convert data structure to JSON
json.loads(jsonObj)                             # Convert JSON to data structure
