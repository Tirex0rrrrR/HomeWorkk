# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Tea:
    def __init__(self, tea_blend: str, tea_spoons: int):
        """
        Инициализация объекта Tea.

        :param tea_blend: Название чайного бленда.
        :param tea_spoons: Количество ложек чая.
        """
        if not isinstance(tea_blend, str):
            raise ValueError("tea_blend должен быть строкой")
        if not isinstance(tea_spoons, int) or tea_spoons < 0:
            raise ValueError("tea_spoons должно быть неотрицательным целым числом")

        self.tea_blend = tea_blend
        self.tea_spoons = tea_spoons

    def adding_welding(self) -> bool:
        """
        Проверяет, можно ли добавить воду в чай.

        :return: True, если количество ложек чая больше 0, иначе False.

        >>> tea = Tea("Peko", 2)
        >>> tea.adding_welding()
        True
        >>> tea = Tea("Peko", 0)
        >>> tea.adding_welding()
        False
        """
        return self.tea_spoons > 0

    def taste_of_tea(self) -> str:
        """
        Определяет вкус чая.

        :return: Строка, описывающая вкус чая.

        >>> tea = Tea("Peko", 2)
        >>> tea.taste_of_tea()
        'Delicious!!!!'
        >>> tea = Tea("Other", 2)
        >>> tea.taste_of_tea()
        'Terrible!!!!'
        """
        if self.tea_blend == "Peko":
            return "Delicious!!!!"
        else:
            return "Terrible!!!!"

    def prepare_tea(self) -> str:
        """
        Приготовить чай.

        :return: Строка, описывающая процесс приготовления чая.

        >>> tea = Tea("Peko", 2)
        >>> tea.prepare_tea()
        'Preparing Peko tea with 2 spoons.'
        """
        return f'Preparing {self.tea_blend} tea with {self.tea_spoons} spoons.'

class Coffee:
    def __init__(self, coffee_blend: str, degree_roasting_coffee: int):
        """
        Инициализация объекта Coffee.

        :param coffee_blend: Название кофейного бленда.
        :param degree_roasting_coffee: Степень обжарки кофе.
        """
        if not isinstance(coffee_blend, str):
            raise ValueError("coffee_blend должен быть строкой")
        if not isinstance(degree_roasting_coffee, int) or degree_roasting_coffee < 0:
            raise ValueError("degree_roasting_coffee должно быть неотрицательным целым числом")

        self.coffee_blend = coffee_blend
        self.degree_roasting_coffee = degree_roasting_coffee

    def grind_coffee(self) -> str:
        """
        Смолоть кофе.

        :return: Строка, описывающая процесс помола кофе.

        >>> coffee = Coffee("Arabica", 3)
        >>> coffee.grind_coffee()
        'Grinding Arabica coffee.'
        """
        return f'Grinding {self.coffee_blend} coffee.'

    def brew_coffee(self) -> str:
        """
        Заварить кофе.

        :return: Строка, описывающая процесс заваривания кофе.

        >>> coffee = Coffee("Arabica", 3)
        >>> coffee.brew_coffee()
        'Brewing Arabica coffee with roasting degree 3.'
        """
        return f'Brewing {self.coffee_blend} coffee with roasting degree {self.degree_roasting_coffee}.'

class Cup:
    def __init__(self, cup_material: str, cup_volume: int):
        """
        Инициализация объекта Cup.

        :param cup_material: Материал чашки.
        :param cup_volume: Объем чашки.
        """
        if not isinstance(cup_material, str):
            raise ValueError("cup_material должен быть строкой")
        if not isinstance(cup_volume, int) or cup_volume <= 0:
            raise ValueError("cup_volume должно быть положительным целым числом")

        self.cup_material = cup_material
        self.cup_volume = cup_volume

    def fill_cup(self, liquid: str) -> str:
        """
        Наполнить чашку жидкостью.

        :param liquid: Название жидкости.
        :return: Строка, описывающая процесс наполнения чашки.

        >>> cup = Cup("Ceramic", 300)
        >>> cup.fill_cup("Water")
        'Filling Ceramic cup with Water.'
        """
        return f'Filling {self.cup_material} cup with {liquid}.'

    def wash_cup(self) -> str:
        """
        Помыть чашку.

        :return: Строка, описывающая процесс мытья чашки.

        >>> cup = Cup("Ceramic", 300)
        >>> cup.wash_cup()
        'Washing Ceramic cup.'
        """
        return f'Washing {self.cup_material} cup.'

if __name__ == "__main__":
    doctest.testmod()

    # TODO работоспособность экземпляров класса проверить с помощью doctest
