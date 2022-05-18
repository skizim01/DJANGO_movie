from django.db import models


class Country(models.Model):
    name = models.CharField("Назва", max_length=100)
    soldat = models.IntegerField("Кількість солдат тисячі")
    money = models.IntegerField("Витрати на оборону в мільйонах доларів")
    m_vvp = models.FloatField("Витрати на оборону в відсотках ВВП")
    s_1000 = models.FloatField("Кількість солдат на тисячу населення")


    class Meta:
        verbose_name = "Країна"
        verbose_name_plural = "Країни"

    def __str__(self):
        return self.name


class OBT(models.Model):
    name = models.CharField("Назва ОБТ", max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Країна виробник ОБТ", max_length=100, null=True,
                               )
    weapon = models.CharField("Основне озброєння ОБТ", max_length=100)
    speed = models.CharField("Швидкість ходу ОБТ", max_length=100)
    range = models.CharField("Запас ходу ОБТ", max_length=100)


class Plane(models.Model):
    name = models.CharField("Назва літака", max_length=100)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, verbose_name="Країна виробник літака", max_length=100,
                                 null=True)
    weapon = models.CharField("Основне озброєння літака", max_length=100, null=True)
    appointment = models.CharField("Призначення літака", max_length=100)
    range = models.CharField("Дальність польоту", max_length=100)

    class Meta:
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"


class Ship(models.Model):
    name = models.CharField("Серія корабля", max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Країна виробник корабля", max_length=100, null=True
                        )
    displacement = models.CharField("Водотоннажність", max_length=100)
    appointment = models.CharField("Призначення корабля", max_length=100)
    autonomy = models.CharField("Автономність плавання", max_length=100)
    year = models.IntegerField("Рік спуску на воду", default=2012)

    class Meta:
        verbose_name = "Корабель"
        verbose_name_plural = "Кораблі"


class Rocket(models.Model):
    name = models.CharField("Назва ракети", max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,verbose_name="Країна виробник ракети", max_length=100,
                              null=True)
    height = models.CharField("Висота польту ракети", max_length=100)
    year = models.IntegerField("Рік поставки на озброєння", default=2012)
    range = models.CharField("Глибина ураження", max_length=100)
    speed = models.CharField("Швидкість польоту ракети", max_length=100, null=True)


    class Meta:
        verbose_name = "Ракета"
        verbose_name_plural = "Дакети"


class Weapon(models.Model):
    name = models.CharField("Назва зброї", max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,verbose_name="Країна виробник зброї", max_length=100, null=True)
    caliber = models.CharField("Калібр зброї", max_length=100)
    range = models.CharField("Прицільна дальність", max_length=100)
    spm = models.CharField("Скорострільність", max_length=100)
    class Meta:
        verbose_name = "Ствольна зброя"
        verbose_name_plural = "Ствольна зброя"


class Ammunition(models.Model):
    name = models.CharField("Назва снаряду", max_length=100)
    caliber = models.CharField("Калібр снаряду", max_length=100)
    type = models.CharField("Тип снаряду", max_length=100)
    appointment = models.CharField("Призначення снаряду", max_length=100)
    range = models.CharField("Дальність польоту снаряду", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Снаряд"
        verbose_name_plural = "Снаряди"


class Artillery(models.Model):
    name = models.CharField("Назва артилерії", max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Країна виробник артилерії", max_length=100,
                               null=True)
    ammunition = models.ManyToManyField( Ammunition, verbose_name="Сумісні снаряди", max_length=100, null=True)
    range = models.CharField("Запас ходу", max_length=100)
    range_move = models.CharField("Тип шасі", max_length=100)
    spm = models.IntegerField("Кількість пострілів в хвилину", default=6)

    class Meta:
        verbose_name = "Артилерія"
        verbose_name_plural = "Артилерія"


class Request(models.Model):
    text = models.TextField(max_length=2000)
    model = models.CharField(max_length=30, null=True)