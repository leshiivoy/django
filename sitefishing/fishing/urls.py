from django.urls import path, re_path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('categ/<int:cat_id>/', views.categories, name='categ_id'),
    path('categ/<slug:cat_slug>/', views.categories_by_slug, name='categ'),
    path('archive/<year4:year>/', views.archive, name='archive'),
]