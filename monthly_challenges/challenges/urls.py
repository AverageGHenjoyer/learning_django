from django.urls import path
from . import views

urlpatterns = [
    path("", views.index), # /challenges/
    path("<int:month>/", views.monthly_challenge_by_number), # /challenges/number
    path("<str:month>/", views.monthly_challenge, name="month-challenge") # /challenges/month
]