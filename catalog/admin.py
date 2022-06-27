from django.contrib import admin
from .models import  Building, Floor, Room, Employee, Workplace, post, departament

# Register your models here.

admin.site.register(Building)
@admin.register(Floor)
class Floor(admin.ModelAdmin):
    model = Floor
    fields = []

@admin.register(Room)
class Room(admin.ModelAdmin):
    model = Room
    fields = []

@admin.register(Employee)
class Employee(admin.ModelAdmin):
    model = Employee
    fields = []

@admin.register(Workplace)
class Workplace(admin.ModelAdmin):
    model = Workplace
    fields = []

@admin.register(departament)
class departament(admin.ModelAdmin):
    model = departament
    fields = []

@admin.register(post)
class post(admin.ModelAdmin):
    model = post
    fields = []