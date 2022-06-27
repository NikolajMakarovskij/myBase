from django.db import models
from django.urls import reverse
import uuid # Required for unique book instances

# Create your models here.

class Building(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField('Building',max_length=200)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
    class Meta:
        verbose_name_plural = 'Здание'

class Floor(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=15, help_text="Введите номер этажа")
    Building = models.ForeignKey('Building', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
    class Meta:
        verbose_name_plural = 'Этаж'


class Room(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=15, help_text="Введите номер кабинета")
    Building = models.ForeignKey('Building', on_delete=models.SET_NULL,blank=True, null=True)
    Floor = models.ForeignKey('Floor', on_delete=models.SET_NULL,blank=True, null=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
    class Meta:
        verbose_name_plural = 'Кабинет'

class Employee(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=50, help_text="Введите ФИО сотрудника")
    Building = models.ForeignKey('Building', on_delete=models.SET_NULL,blank=True, null=True)
    Floor = models.ForeignKey('Floor', on_delete=models.SET_NULL,blank=True, null=True)
    Room = models.ForeignKey('Room', on_delete=models.SET_NULL,blank=True, null=True)
    Workplace = models.ForeignKey('Workplace', on_delete=models.SET_NULL,blank=True, null=True)
    departament = models.ForeignKey('departament', on_delete=models.SET_NULL,blank=True, null=True)
    post = models.ForeignKey('Post', on_delete=models.SET_NULL,blank=True, null=True)


    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
    class Meta:
        verbose_name_plural = 'Сотрудник'

class Workplace(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=50, help_text="Введите номер рабочего места")
    Building = models.ForeignKey('Building', on_delete=models.SET_NULL,blank=True, null=True)
    Floor = models.ForeignKey('Floor', on_delete=models.SET_NULL,blank=True, null=True)
    Room = models.ForeignKey('Room', on_delete=models.SET_NULL,blank=True, null=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
    class Meta:
        verbose_name_plural = 'Рабочее место'

class departament(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=50, help_text="Введите название отдела")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
    class Meta:
        verbose_name_plural = 'Отдел'

class post(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=50, help_text="Введите должность")
    departament = models.ForeignKey('departament', on_delete=models.SET_NULL,blank=True, null=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
    class Meta:
        verbose_name_plural = 'Должность'