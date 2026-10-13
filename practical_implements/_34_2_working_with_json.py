import json

with open("_34_3_json_data.json") as f:
    data = json.load(f)

for state in data["states"]:
    print(state)

for state in data["states"]:
    print(state["name"], state["abbreviation"])

for state in data["states"]:
    del state["area_codes"]

with open("_34_4_json_changes.json", "w") as f:
    json.dump(data, f, indent=2)
