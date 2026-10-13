from collections import namedtuple


nik_dict = {
    'name': 'Nik',
    'age': 33,
    'location': 'toronto',
    'website': 'datagy'
}

print(nik_dict['name'])

Person = namedtuple('Person', ['Name', 'Age', 'Location', 'Website'])

nik = Person('Nik', 33, 'Toronto', 'Datagy')

print(nik)

print(type(nik))

print(issubclass(Person, tuple))

print(nik[0])

print(nik.Name)
print(nik.Age)

Employee = namedtuple('Employee', ['Name', 'Age', 'Location', 'Company'], defaults = [23, 'Toronto', 'Datagy'])

joe = Employee('Joe', 23)
print(joe)

jane = Employee('Jane')
print(jane)

print(Employee._field_defaults)

new_joe = joe._replace(Location = 'New York')
print(joe)
print(new_joe)

joe_dict = new_joe._asdict()
print(joe_dict)

Employee = namedtuple('Employee', ['Name', 'from', 'Age'], rename = True)

print(Employee._fields)
