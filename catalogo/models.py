from django.db import models

class Obra (models.Model):
    TIPO_CHOICE = [
        ("Filme", "Filme"),
        ("Série", "Série"),
    ]

    titulo = models.CharField(max_length=150)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICE)
    ano = models.IntegerField()
    genero = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

#python manage.py makemigrations
#python manage.py migrate
#python manage.py createsuperuser
#poe o nome, email e senha, depois entra no admin do django e adiciona algumas obras
#python manage.py runserver
