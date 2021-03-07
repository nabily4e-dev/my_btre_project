from django.contrib import admin
from django.db import models
from .models import Realtor


class RealtorsAdmin(admin.ModelAdmin):
    """"""
    
    list_display = ('id', 'name', 'name', 'hire_date', )
    list_display_links = ('id', 'name', )
    search_fields = ('name', )
    list_per_page = 25


admin.site.register(Realtor, RealtorsAdmin)

class defineNew(models.Model):
    """The try of all tries!"""