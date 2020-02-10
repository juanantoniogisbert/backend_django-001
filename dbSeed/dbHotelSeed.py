import random
from faker import Faker

from hotel.models import Hotel

fake = Faker()

for i in range(5):
    hotel = Hotel()

    hotel.name = fake.name()
    hotel.location = fake.address()
    hotel.stars = random.randint(1,5)

    hotel.save()

#    print(i)
