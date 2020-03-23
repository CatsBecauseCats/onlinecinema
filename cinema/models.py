from django.db import models

class Persona(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        name = self.first_name + " " + self.last_name
        return name

class Film(models.Model):
    film_name = models.CharField(max_length=40)
    year = models.DateField()
    creator_name = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='+')
    actors = models.ManyToManyField(Persona)

    def __str__(self):
        return self.film_name

class MovieViewsPerWeek(models.Model):
    film = models.OneToOneField(
        Film,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    data = models.DateField()
    count_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.film) + ": " + str(self.count_views)
