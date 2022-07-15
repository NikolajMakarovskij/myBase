from django.contrib import admin
from .models import  OS, Building, Floor, Room, Employee, Workplace, monitor, motherboard, post, departament, software, workstation

@admin.register(Building)
class Building(admin.ModelAdmin):
    model = Building
    fields = []

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

@admin.register(workstation)
class workstation(admin.ModelAdmin):
    model = workstation
    fields = [('name', 'manufacturer'), 
        ('Workplace', 'Employee'),
        ('serial', 'serialImg'),
        ('invent','inventImg'),
        ('motherboard','monitor', 'OS'),
        'CPU','GPU', 'RAM', 'SSD', 'HDD',
        'DCPower', 'keyBoard', 'mouse',
        ]

@admin.register(software)
class software(admin.ModelAdmin):
    model = software
    fields = []

@admin.register(OS)
class OS(admin.ModelAdmin):
    model = OS
    fields = []

@admin.register(monitor)
class monitor(admin.ModelAdmin):
    model = monitor
    fields = [
        ('name','manufacturer'),
        ('serial','serialImg'),
        ('invent','inventImg'),

    ]

@admin.register(motherboard)
class motherboard(admin.ModelAdmin):
    model = motherboard
    fields = [
        ('name','manufacturer'),
        ('serial','serialImg'),
        'CPUSoket', 'RAMSlot', 'USBPort',
        'COMPort', 'PCI_E', 'PCI', 'VGA',
        'SATA', 'HDMI', 'DispayPort',
        'powerSupply', 'powerSupplyCPU',
    ]