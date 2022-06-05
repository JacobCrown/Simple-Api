from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def pesel_validator(value):
    if not value.isdecimal():
        raise ValidationError(
            _('%(value)s is not a valid pesel'),
            params={'value': value},
        )
    


class Student(models.Model):
    id_stud = models.BigAutoField(primary_key=True)
    indeks = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(999999),
            MinValueValidator(100000)
        ],
        unique=True
     )
    imie = models.CharField(max_length=80)
    nazwisko = models.CharField(max_length=80)
    pesel = models.CharField(
        max_length=11,
        validators=[
            pesel_validator,
            MinLengthValidator(11)
        ],
        unique=True
     )

    def __str__(self):
        return f'Student {self.id_stud}: {self.imie} {self.nazwisko} ' \
            f'indeks: {self.indeks}, pesel: {self.pesel}'

    class Meta:
        ordering = ['id_stud']
         

    