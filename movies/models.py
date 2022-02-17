from django.db import models

from django.urls import reverse


class Techers(models.Model):
    name = models.CharField("Імя", max_length=100)
    description = models.TextField("Опис")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"


class Specialty(models.Model):
    name = models.CharField("Спеціальність", max_length=150)
    description = models.TextField("Опис")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Спеціальність"
        verbose_name_plural = "Спеціальності"


class Category(models.Model):
    name = models.CharField("Дисципліна", max_length=150)
    description = models.TextField("Опис")
    techers = models.ManyToManyField(Techers, verbose_name="Викладачі", related_name="techers" )
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дисципліна"
        verbose_name_plural = "Дисципліни"


class Students(models.Model):
    name = models.CharField("Імя", max_length=100)
    expectation = models.TextField("Очікування")
    specialty = models.ForeignKey(Specialty,
                                  verbose_name="Спеціальність",
                                  on_delete=models.CASCADE,
                                 null=True)
    age = models.PositiveSmallIntegerField("Вік", default=0)
    category = models.ForeignKey(Category,
                                 verbose_name="Дисципліна",
                                 on_delete=models.CASCADE,
                                 null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("actor_detail", kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Cтудент"
        verbose_name_plural = "Cтуденти"


