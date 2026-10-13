from collections import defaultdict

data = defaultdict()

print(data)
print(type(data))
print(issubclass(defaultdict, dict))

inventory = {'Computer': 1, 'TV': 2, 'Phone': 3}
inventory['Phone'] += 1

print(inventory)

if 'VCRs' in inventory:
    inventory['VCRs'] += 1
else:
    inventory['VCRs'] = 1

print(inventory)

inventory_dd : defaultdict[str, int] = defaultdict(int)
print(inventory_dd)

inventory_dd['VCRs'] += 100
inventory_dd['Phones'] += 1
print(inventory_dd)

users = {
    'Nik': 'Toronto',
    'Kate': 'Toronto',
    'Evan': 'London',
    'Kyra': 'New York',
    'Jeff': 'New York',
}

locations_old: dict = {}
for person, location in users.items():
    if location in locations_old:
        locations_old[location].append(person)
    else:
        locations_old[location] = [person]

print(locations_old)

locations: defaultdict = defaultdict(list)

for person, location in users.items():
    locations[location].append(person)

print(locations)

aggregate = defaultdict(float)

sales = [
    ('April', 'TVs', 5342.46),
    ('April', 'Phones', 423.32),
    ('April', 'Computers', 1234.43),
    ('May', 'VCRs', 23423.23),
    ('May', 'TVs', 3213.24),
    ('May', 'Phones', 12356.32),
    ('May', 'Computers', 5435.32),
    ('June', 'TVs', 123.43),
]

for _, item, amount in sales:
    aggregate[item] += amount

    print(aggregate)