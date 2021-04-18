from django.urls import path
from .views import main, north_america, europe, country, AddComment, filter_form, filter_country

urlpatterns = [
    path('', main, name='main'),
    path('north_america', north_america, name='north_america'),
    path('europe', europe, name='europe'),
    path('details', country, name='country'),
    path('add_comment', AddComment.as_view(), name='add_comment'),
    path('filter_form', filter_form, name='filter_form'),
    path('filter_country', filter_country, name='filter_country'),
]
