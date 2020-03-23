from django.contrib import admin
from .models import Persona, Film, MovieViewsPerWeek

admin.site.register(Persona)
admin.site.register(Film)
admin.site.register(MovieViewsPerWeek)