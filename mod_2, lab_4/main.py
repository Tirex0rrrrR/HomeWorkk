class Car:
    def __init__(self, max_speed: int, distance_traveled: float, fuel_tank_number: int, weight_auto: float, engine_volume: float):
        """
        Инициализация объекта Car.

        :param max_speed: Максимальная скорость автомобиля.
        :param distance_traveled: Пробег автомобиля.
        :param fuel_tank_number: Объем топливного бака.
        :param weight_auto: Вес автомобиля.
        :param engine_volume: Объем двигателя.
        """
        self.max_speed = max_speed
        self.engine_volume = engine_volume
        self.weight_auto = weight_auto
        self.fuel_tank_number = fuel_tank_number
        self.distance_traveled = distance_traveled
        self.power_engine = engine_volume * 45

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Car.

        :return: Строка с описанием автомобиля.
        """
        return (f'Максимальная скорость автомобиля: {self.max_speed}, '
                f'Обьем двигателя автомобиля: {self.engine_volume}, '
                f'Вес автомобиля: {self.weight_auto}, '
                f'Обьем бака автомобиля: {self.fuel_tank_number}, '
                f'Расстояние, которое проехал за сегодня автомобиль: {self.distance_traveled}, '
                f'Мощьность двигателя автомобиля: {self.power_engine}, ')

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта Car.

        :return: Строка с параметрами автомобиля.
        """
        return (f"Car(max_speed={self.max_speed}, distance_traveled={self.distance_traveled}, "
                f"fuel_tank_number={self.fuel_tank_number}, weight_auto={self.weight_auto}, "
                f"engine_volume={self.engine_volume}, power_engine={self.power_engine})")

    def fuel_consumption(self) -> float:
        """
        Рассчитывает расход топлива.

        :return: Расход топлива в литрах на 100 км.
        """
        consumption = (0.25 * self.weight_auto * self.power_engine) / 1000
        return consumption

    def remaining_fuel(self) -> float:
        """
        Рассчитывает оставшееся количество топлива.

        :return: Оставшееся количество топлива в литрах.
        """
        return self.fuel_tank_number - (self.distance_traveled / 100 * self.fuel_consumption())

    def fuel_per_distance(self) -> float:
        """
        Рассчитывает количество топлива на расстояние.

        :return: Количество потребленного топлива в литрах.
        """
        return self.fuel_tank_number - self.remaining_fuel()

class Passenger_car(Car):
    def __init__(self, max_speed: int, distance_traveled: float, fuel_tank_number: int, weight_auto: float, engine_volume: float, roof_availability: bool):
        """
        Инициализация объекта Passenger_car.

        :param max_speed: Максимальная скорость автомобиля.
        :param distance_traveled: Пробег автомобиля.
        :param fuel_tank_number: Объем топливного бака.
        :param weight_auto: Вес автомобиля.
        :param engine_volume: Объем двигателя.
        :param roof_availability: Наличие крыши.
        """
        super().__init__(max_speed, distance_traveled, engine_volume, fuel_tank_number, weight_auto)
        self.roof_availability = roof_availability

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Passenger_car.

        :return: Строка с описанием автомобиля и наличием крыши.
        """
        base_str = super().__str__()
        if self.roof_availability:
            return base_str + "Автомобиль с крышей!"
        else:
            return base_str + "Автомобиль без крыши!"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта Passenger_car.

        :return: Строка с параметрами автомобиля и наличием крыши.
        """
        return super().__repr__()[:-1] + f", roof_availability={self.roof_availability})"

    def car_type(self) -> str:
        """
        Определяет тип автомобиля на основе наличия крыши.

        :return: Тип автомобиля ("Sedan" или "Convertible").
        """
        if self.roof_availability:
            return "Sedan"
        else:
            return "Convertible"

class Cargo_truck(Car):
    def __init__(self, max_speed: int, distance_traveled: float, fuel_tank_number: int, weight_auto: float, engine_volume: float, cargo_weight: float, number_of_fuel_tanks: int):
        """
        Инициализация объекта Cargo_truck.

        :param max_speed: Максимальная скорость автомобиля.
        :param distance_traveled: Пробег автомобиля.
        :param fuel_tank_number: Объем топливного бака.
        :param weight_auto: Вес автомобиля.
        :param engine_volume: Объем двигателя.
        :param cargo_weight: Вес груза.
        :param number_of_fuel_tanks: Количество топливных баков.
        """
        super().__init__(max_speed, distance_traveled, engine_volume, fuel_tank_number, weight_auto)
        self.__number_of_fuel_tanks = number_of_fuel_tanks
        self.__cargo_weight = cargo_weight

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Ser_car.

        :return: Строка с описанием автомобиля, количеством топливных баков и весом груза.
        """
        base_str = super().__str__()
        return base_str + f'Количество топливных баков у автомобиля: {self.__number_of_fuel_tanks}, ' \
                          f'Вес груза автомобиля: {self.__cargo_weight}'

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта Ser_car.

        :return: Строка с параметрами автомобиля, количеством топливных баков и весом груза.
        """
        return super().__repr__()[:-1] + f", number_of_fuel_tanks={self.__number_of_fuel_tanks}, " \
                                         f"cargo_weight={self.__cargo_weight})"

    def fuel_consumption(self) -> float:
        """
        Перегруженный метод для расчета расхода топлива с учетом веса груза.

        :return: Расход топлива в литрах на 100 км с учетом веса груза.
        """
        percentage_of_seedlings = (self.weight_auto + self.__cargo_weight) / self.weight_auto - 1
        return super().fuel_consumption() + ((super().fuel_consumption() / 100) * percentage_of_seedlings)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    car = Passenger_car(2, 55, 33, 22, 11, True)
    print(car.__str__())
    print(car.__repr__())
