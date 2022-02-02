from django.urls import path
from . import views

app_name = 'nypl_endpoint_app'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /random/
    path('random/',
         views.RandomItemView.as_view(), name='random_item'),
]
