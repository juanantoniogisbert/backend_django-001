from faker import Faker

from hotel.models import Hotel

fake = Faker()

for i in range(1000):
    hotel = Hotel()

    hotel.name = fake.name()
    hotel.location = fake.address()
    hotel.stars = 5

    hotel.save()

#    print(i)
