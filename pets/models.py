from django.db import models

# Create your models here.

class Kind(models.Model):
    CAT = 'CT'
    DOG = 'DG'
    PARROT = 'PT'

    KIND_OF_ANIMAL_CHOICES = (
        (CAT, 'Cat'),
        (DOG, 'Dog'),
        (PARROT, 'Parrot'),
    )

    kind_of_animal = models.CharField('Вид животного', max_length=2, choices=KIND_OF_ANIMAL_CHOICES)

    def __str__(self):
        return self.kind_of_animal

class Breed(models.Model):
    name = models.CharField('Порода', max_length=256)
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE, null=True, verbose_name='Вид животного')

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField('Кличка', max_length=256)
    age = models.CharField('Возраст', max_length=20)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name='Порода')
    info = models.TextField('Описание')
    photo = models.ImageField(upload_to='pets_photo', blank=True)

    def __str__(self):
        return self.name
    

    

  

