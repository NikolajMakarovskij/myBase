from operator import index
from django.urls import path
from . import views
from django.urls import include, re_path

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^rooms/$', views.RoomListView.as_view(), name='room'),
    re_path(r'^workplaceyes/$', views.WorkplaceListView.as_view(), name='workplace'),
    re_path(r'^employeyes/$', views.EmployeeListView.as_view(), name='employee'),
    re_path(r'^software/$', views.softwareListView.as_view(), name='software'),
    re_path(r'^workstation/$', views.workstationListView.as_view(), name='workstation'),
    
]