from django.urls import path
from .views import list_do, home, detail_do, add_do, dell_do

urlpatterns = [
    path('', home, name='home'),
    path('list_do/', list_do, name='list_do'),
    path('detail_do/<int:id>/', detail_do, name='detail_do'),
    path('add_do/', add_do, name='add_do'),
    path('dell/<int:id>', dell_do, name='dell_do'),
]
