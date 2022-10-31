from django.urls import path
from produto import views


app_name = 'produto'

urlpatterns = [
    path("", views.index, name="index")
]