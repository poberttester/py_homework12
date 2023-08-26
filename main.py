# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.


class Student:
    def __init__(self, soname, name: str, last_name):
        self.__name = name
        self.__soname = soname
        self.__last_name = last_name

    def __getName__(self):
        return self.__name

    def __getSoname__(self):
        return self.__soname

    def __getLast_name__(self):
        return self.__last_name

    def __setName__(self, value):
        if value.isalpha():
            if value.istitle():
                self.__name = value
            else:
                raise TypeError("Значение в поле 'name' должно начинаться с заглавной буквы")
        else:
            raise TypeError("В поле 'name' должны быть переданы только алфавитные символы")

    def __setSoname__(self, value):
        if value.isalpha():
            if value.istitle():
                self.__soname = value
            else:
                raise TypeError("Значение в поле 'soname' должно начинаться с заглавной буквы")
        else:
            raise TypeError("В поле 'soname' должны быть переданы только алфавитные символы")

    def __setLast_name__(self, value):
        if value.isalpha():
            if value.istitle():
                self.__last_name = value
            else:
                raise TypeError("Значение в поле 'last_name' должно начинаться с заглавной буквы")
        else:
            raise TypeError("В поле 'last_name' должны быть переданы только алфавитные символы")


if __name__ == '__main__':
    student = Student('Feborov', 'Ivan', 'Vladimirovich')
    print(student.__getLast_name__())
    student.__setLast_name__('Nicolas')
    print(student.__getLast_name__())
