from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path("Need_of_password", views.Need_of_password, name="Need_of_password"),
    path("contact_us", views.contact_us, name="contact_us"),
    # path("pass_gen", views.pass_gen, name="pass_gen"),
]