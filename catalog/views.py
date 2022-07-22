from unicodedata import name
from django.shortcuts import render
from .models import Building, Employee, Workplace, software, workstation
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
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

class EmployeeListView(generic.ListView):
    model = Employee
    paginate_by =  10

class WorkplaceListView(generic.ListView):
    model = Workplace
    paginate_by =  10

def workplace_list(request): 
    return render(
        request,
        'workplace_list.html',
        context={
            'workplace_list.html':workplace_list,
        }
    )

class workstationListView(generic.ListView):
    model = workstation
    paginate_by =  10

def workstation_list(request): 
    return render(
        request,
        'workstation_list.html',
        context={
            'workstation_list.html':workstation_list,
        }
    )

class workstationDetailView(generic.DetailView):
    model = workstation

def workstation_detail_view(request,pk):
    try:
        workstation_id=workstation.objects.get(pk=pk)
    except workstation.DoesNotExist:
        raise Http404("Не удалось найти детальную информацию")

    return render(
        request,
        'catalog/workstation_detail.html',
        context={'workstation':workstation_id,}
    )

class softwareListView(generic.ListView):
    model = software
    paginate_by =  10

def software_list(request):
    return render(
        request,
        'software_list.html',
        context={
          'software_list.html':software_list,
        }
    )

class AuthorUpdate(UpdateView):
    model = Building
    fields = ['name']