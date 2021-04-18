from django.shortcuts import render
from .models import Country, Comment
from urllib.parse import unquote
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CountryForm


def main(request):
    return render(request, 'main.html')


def europe(request):
    europe_countries = Country.objects.filter(continent__name='Европа')
    return render(request, 'list.html', {'list_items': europe_countries, 'parent_name': 'Европа'})


def north_america(request):
    north_america_countries = Country.objects.filter(continent__name='Северная Америка')
    return render(request, 'list.html', {'list_items': north_america_countries, 'parent_name': 'Северная Америка'})


def country(request):
    requested_country = Country.objects.get(name=unquote(request.GET['country']))
    comments = Comment.objects.filter(country__name=requested_country.name)
    data = {'country_name': request.GET['country'], 'requested_country': requested_country, 'comments': comments}
    return render(request, 'details.html', context=data)


class AddComment(CreateView):
    model = Comment
    fields = ['country', 'name', 'comment', 'rating']
    template_name = 'comment.html'
    success_url = reverse_lazy('main')


def filter_form(request):
    form = CountryForm()
    return render(request, 'filter_form.html', {'form': form})


def filter_country(request):
    sea = ''
    mountain = ''
    visa = ''

    form = CountryForm(request.POST)
    if form.is_valid():
        sea = form.cleaned_data.get("sea")
        mountain = form.cleaned_data.get("mountain")
        visa = form.cleaned_data.get("visa")

    requested_country = Country.objects.filter(sea=sea, mountain=mountain, visa=visa)

    return render(request, 'filter_country.html', {'requested_country': requested_country})
