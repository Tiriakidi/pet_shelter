from django.contrib import admin
from pets.models import Pet, Breed, Kind

# Register your models here.

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    @staticmethod
    def kind_name(obj):
        return obj.kind.kind_of_animal
    
    list_display = ('name', 'breed', 'photo')
    fields = ('name', 'age', 'breed', 'info', 'photo')

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass

@admin.register(Kind)
class KindAdmin(admin.ModelAdmin):
    pass

