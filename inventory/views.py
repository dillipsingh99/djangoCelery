from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from . models import Person, City
from . forms import PersonForm


# class PersonListView(ListView):
#     model = Person
#     # template_name = 'person_list.html'
#     context_object_name = 'people'


def personlist(request):
    # data = Person.objects.all()
    name = 'Test1'
    data = Person.objects.raw('select * from inventory_person where name=%s', [name])
    # filter(country__startswith='Ne').values('name', 'birthdate','city', 'country',)
    return render(request, 'person_list.html', {'data':data})


class PersonCreateView(CreateView):
    model = Person
    template_name = 'person_add.html'
    form_class = PersonForm
    # fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('person_changelist')

class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    # fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('person_changeList')

def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})