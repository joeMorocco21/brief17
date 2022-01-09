from django.contrib import admin
from .models import data_view

# Register your models here.
class Departement(admin.ModelAdmin):
    # define which columns displayed in changelist
    list_display = ('id','departement','ville')
    # add filtering by date
    list_filter = ('departement',)
    # add search field 
    search_fields = ['departement']

admin.site.register(data_view, Departement)