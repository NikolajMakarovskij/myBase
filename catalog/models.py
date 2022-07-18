from django.db import models
from django.urls import reverse
import uuid 

class Building(models.Model):
    name = models.CharField('Building',max_length=200)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
    class Meta:
        verbose_name_plural = 'Здание'

class Floor(models.Model):
    name = models.CharField(max_length=15, help_text="Введите номер этажа")
    Building = models.ForeignKey('Building', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Этаж'


class Room(models.Model):
    name = models.CharField(max_length=15, help_text="Введите номер кабинета")
    Building = models.ForeignKey('Building', on_delete=models.SET_NULL,blank=True, null=True)
    Floor = models.ForeignKey('Floor', on_delete=models.SET_NULL,blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Кабинет'
        ordering = ["Building", "Floor", "name"]

class Employee(models.Model):
    name = models.CharField(max_length=50, help_text="Введите ФИО сотрудника")
    Workplace = models.ForeignKey('Workplace', on_delete=models.SET_NULL,blank=True, null=True)
    departament = models.ForeignKey('departament', on_delete=models.SET_NULL,blank=True, null=True)
    post = models.ForeignKey('Post', on_delete=models.SET_NULL,blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Сотрудник'
        ordering = ["name", "Workplace"]

class Workplace(models.Model):
    name = models.CharField(max_length=50, help_text="Введите номер рабочего места")
    Room = models.ForeignKey('Room', on_delete=models.SET_NULL,blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Рабочее место'
        ordering = ["name","Room"]

class departament(models.Model):
    name = models.CharField(max_length=50, help_text="Введите название отдела")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Отдел'

class post(models.Model):
    name = models.CharField(max_length=50, help_text="Введите должность")
    departament = models.ForeignKey('departament', on_delete=models.SET_NULL,blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Должность'

class software (models.Model):
    name = models.CharField(max_length=50, help_text="ВВедите название ПО")
    workstation = models.ForeignKey('workstation', on_delete=models.SET_NULL,blank=True, null=True)
    Employee = models.ForeignKey('Employee', on_delete=models.SET_NULL,blank=True, null=True)
    manufacturer = models.CharField(max_length=200, blank=True, help_text="Описание производителя")
    licenseKeyText = models.CharField(max_length=50, blank=True, null=True, help_text="Введите лицензтонный ключ")
    licenseKeyImg = models.ImageField(upload_to='soft/', blank=True, null=True, help_text="прикрепите файл")
    licenseKeyFile = models.FileField(upload_to='soft/', blank=True, null=True, help_text="прикрепите файл")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'ПО'
        ordering = [ "Employee", "name"]

class OS (models.Model):
    name = models.CharField(max_length=50, help_text="Введите Название ОС")
    licenseKeyText = models.CharField(max_length=50, blank=True, null=True, help_text="Введите лицензтонный ключ")
    licenseKeyImg = models.ImageField(upload_to='OS/', blank=True, null=True, help_text="прикрепите файл")
    licenseKeyFile = models.FileField(upload_to='soft/', blank=True, null=True, help_text="прикрепите файл")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'ОС'

class workstation(models.Model):
    name = models.CharField(max_length=50, blank=True, help_text="Введите номер станции")
    Workplace = models.ForeignKey('Workplace', on_delete=models.SET_NULL,blank=True, null=True)
    Employee = models.ForeignKey('Employee', on_delete=models.SET_NULL,blank=True, null=True)
    OS = models.ForeignKey('OS', on_delete=models.SET_NULL,blank=True, null=True)
    serial = models.CharField(max_length=50, blank=True, help_text="Введите серийный номер")
    serialImg = models.ImageField(upload_to='workstation/serial/', blank=True, null=True, help_text="прикрепите файл")
    invent = models.CharField(max_length=50, blank=True, help_text="Введите инвентаризационный номер")
    inventImg = models.ImageField(upload_to='workstation/invent/', blank=True, null=True, help_text="прикрепите файл")
    manufacturer = models.CharField(max_length=200, blank=True, help_text="Описание производителя")
    modelComputer = models.CharField(max_length=200, blank=True, help_text="Введите название модели")
    motherboard = models.ForeignKey('motherboard', on_delete=models.SET_NULL, blank=True, null=True)
    monitor = models.ForeignKey('monitor', on_delete=models.SET_NULL,blank=True, null=True)
    CPU = models.TextField(max_length=200, blank=True, help_text="Описание CPU")
    GPU = models.TextField(max_length=200, blank=True, help_text="Описание GPU")
    RAM = models.TextField(max_length=200, blank=True, help_text="Описание RAM")
    SSD = models.TextField(max_length=200, blank=True, help_text="Описание SSD")
    HDD = models.TextField(max_length=200, blank=True, help_text="Описание HDD")
    DCPower = models.TextField(max_length=200, blank=True, help_text="Описание блока питания")
    keyBoard = models.TextField(max_length=200, blank=True, help_text="Описание клавиатуры")
    mouse = models.TextField(max_length=200, blank=True, help_text="Описание мыши")

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('workstation-detail', args=[str(self.id)])
    class Meta:
        verbose_name_plural = 'Рабочая станция'
        ordering = ["Employee", "name", "Workplace"]

class monitor (models.Model):
    manufacturer = models.CharField(max_length=50, blank=True, help_text="Введите Название производителя")
    name = models.CharField(max_length=50, help_text="Введите Название модели")
    serial = models.CharField(max_length=50, blank=True, help_text="Введите серийный номер")
    serialImg = models.ImageField(upload_to='monitor/serial/', blank=True, null=True, help_text="прикрепите файл")
    invent = models.CharField(max_length=50, blank=True, help_text="Введите инвентаризационный номер")
    inventImg = models.ImageField(upload_to='monitor/invent/', blank=True, null=True, help_text="прикрепите файл")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Монитор'

class motherboard (models.Model):
    manufacturer = models.CharField(max_length=50, blank=True, help_text="Введите Название производителя")
    name = models.CharField(max_length=50, help_text="Введите Название модели")
    serial = models.CharField(max_length=50, blank=True, help_text="Введите серийный номер")
    serialImg = models.ImageField(upload_to='motherboard/soft/', blank=True, null=True, help_text="прикрепите файл")
    CPUSoket = models.TextField(max_length=200, blank=True, help_text="Описание сокета")
    RAMSlot = models.TextField(max_length=200, blank=True, help_text="Описание RAM")
    USBPort = models.TextField(max_length=200, blank=True, help_text="Введите количество и тип ")
    COMPort = models.TextField(max_length=200, blank=True, help_text="Введите количество")
    PCI_E = models.TextField(max_length=200, blank=True, help_text="Введите количество")
    PCI = models.TextField(max_length=200, blank=True, help_text="Введите количество и тип")
    VGA = models.TextField(max_length=200, blank=True, help_text="Введите количество")
    SATA = models.TextField(max_length=200, blank=True, help_text="Введите количество")
    HDMI = models.TextField(max_length=200, blank=True, help_text="Введите количество")
    DispayPort = models.TextField(max_length=200, blank=True, help_text="Введите количество")
    powerSupply = models.TextField(max_length=200, blank=True, help_text="Введите конфигурацию")
    powerSupplyCPU = models.TextField(max_length=200, blank=True, help_text="Введите конфигурацию")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Материнская плата'




