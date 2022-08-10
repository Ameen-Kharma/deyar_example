from ..models import Car


class CarRepository():
    """
    this is used to perform the ORM operation and all database operations
    """
    def get_base_query(self, filters=None, **options):
        return Car.objects.all()

    def get_cars(self, filters=None):
        query = self.get_base_query(filters)
        return query.all()

    def add_car(self, name):
        car = Car(name="car")
        car.save()

        return car
