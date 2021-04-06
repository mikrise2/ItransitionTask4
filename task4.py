from mimesis import Person
from mimesis import Address
import csv
import sys

quantity = int(sys.argv[1])
language = sys.argv[2]
person = Person(language)
address = Address(language)
listForCVS = []

writer = csv.writer(sys.stdout, delimiter=';',
                    escapechar='"', quoting=csv.QUOTE_NONE)
for i in range(0, quantity):
    writer.writerow([person.full_name(), address.country(),
                     address.region(), address.city(), address.address(),
                     address.zip_code(),
                     person.telephone()])
