from django.contrib import admin
from .models import Professor

@admin.register(Professor)
class professorAdmin(admin.ModelAdmin):
    list_display = ['nome','cref','id']
