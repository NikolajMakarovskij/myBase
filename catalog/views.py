from unicodedata import name
from django.shortcuts import render
from .models import Building, Floor, Room, Employee, Workplace, departament, post, software, workstation
from django.views import generic
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable.
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={
            'num_visits':num_visits,
        }, 
    )

class BuildingListView(generic.ListView):
    model = Building

class FloorListView(generic.ListView):
    model = Floor

class RoomListView(generic.ListView):
    model = Room

class EmployeeListView(generic.ListView):
    model = Employee

class WorkplaceListView(generic.ListView):
    model = Workplace

def workplace_list(request): 
    buildings=Building.objects.all().order_by("name")
    floors=Floor.objects.all().order_by("name")
    workplaceyes=Workplace.objects.all().order_by("name")
    return render(
        request,
        'workplace_list.html',
        context={
            'workplace_list.html':workplace_list,
            'buildings':buildings,
            'floors':floors,
            'workplaceyes':workplaceyes,

        }
    )

class departamentListView(generic.ListView):
    model = departament

class postListView(generic.ListView):
    model = post

class workstationListView(generic.ListView):
    model = workstation

def workstation_list(request): 
    buildings=Building.objects.all().order_by("name")
    floors=Floor.objects.all().order_by("name")
    workplaceyes=Workplace.objects.all().order_by("name")
    return render(
        request,
        'workstation_list.html',
        context={
            'workstation_list.html':workstation_list,
            'buildings':buildings,
            'floors':floors,
            'workplaceyes':workplaceyes,

        }
    )

class softwareListView(generic.ListView):
    model = software

def software_list(request):
    workstations=workstation.objects.all().order_by(name) 
    return render(
        request,
        'software_list.html',
        context={
            'software_list.html':software_list,
            'workstations':workstations

        }
    )