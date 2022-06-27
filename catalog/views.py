from django.shortcuts import render
from .models import Building, Floor, Room, Employee, Workplace, departament, post
from django.views import generic
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime


# Create your views here.

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_buildings=Building.objects.all().count()
    num_floors=Floor.objects.all().count()
    num_rooms=Room.objects.all().count()
    num_employeyes=Employee.objects.all().count()
    num_workplaceyes=Workplace.objects.all().count()
    num_departaments=departament.objects.all().count()
    num_posts=post.objects.all().count()

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
            'num_buildings':num_buildings,
            'num_floors':num_floors,
            'num_rooms':num_rooms,
            'num_employeyes':num_employeyes,
            'num_workplaceyes':num_workplaceyes,
            'num_departaments':num_departaments,
            'num_posts':num_posts,

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

class departamentListView(generic.ListView):
    model = departament

class postListView(generic.ListView):
    model = post