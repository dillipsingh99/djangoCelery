from django.urls import path

from . import views

urlpatterns = [
    # path('', views.PersonListView.as_view(), name='person_changelist'),
    path('add/', views.PersonCreateView.as_view(), name='person_add'),
    path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_chnage'),
    path('', views.personlist, name='person_changelist'),

    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]