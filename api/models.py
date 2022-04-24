from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator


class Student(models.Model):
    id_stud = models.BigAutoField(primary_key=True)
    indeks = models.CharField(
        max_length=6,
        validators=[
            MaxLengthValidator(6),
            MinLengthValidator(6)
        ],
        unique=True
     )
    imie = models.CharField(max_length=80)
    nazwisko = models.CharField(max_length=80)
    pesel = models.CharField(
        max_length=11,
        validators=[
            MaxLengthValidator(11),
            MinLengthValidator(11)
        ]
     )

    def __str__(self):
        return f'Student {self.id_stud}: {self.imie} {self.nazwisko} ' \
            f'indeks: {self.indeks}, pesel: {self.pesel}'

    class Meta:
        ordering = ['-id_stud']
         

    