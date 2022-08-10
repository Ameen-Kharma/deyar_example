from ..repository.car_repository import CarRepository


class CarComponent():
    """
    this used for applying any needed logic
    """
    @staticmethod
    def is_car_exist(name):
        pass

    @staticmethod
    def get_cars():
        # do any login needed
        return CarRepository().get_cars()

    @staticmethod
    def create_car(name):
        CarComponent.is_car_exist(name)

        return CarRepository().add_car(name)


