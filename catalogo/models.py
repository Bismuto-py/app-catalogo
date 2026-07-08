from django.db import models

<<<<<<< HEAD
class Obra(models.Model):
    TIPO_CHOICES = [
=======
class Obra (models.Model):
    TIPO_CHOICE = [
>>>>>>> 14d9a6abaffd7649db87a8e810b0ef29929e2d41
        ("Filme", "Filme"),
        ("Série", "Série"),
    ]

    titulo = models.CharField(max_length=150)
<<<<<<< HEAD
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    ano = models.IntegerField()
    genero =  models.CharField(max_length=100)
=======
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICE)
    ano = models.IntegerField()
    genero = models.CharField(max_length=100)
>>>>>>> 14d9a6abaffd7649db87a8e810b0ef29929e2d41
    descricao = models.TextField()

    def __str__(self):
        return self.titulo
<<<<<<< HEAD
=======

#python manage.py makemigrations
#python manage.py migrate
#python manage.py createsuperuser
#poe o nome, email e senha, depois entra no admin do django e adiciona algumas obras
#python manage.py runserver
>>>>>>> 14d9a6abaffd7649db87a8e810b0ef29929e2d41
