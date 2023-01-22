from django.urls import path
from .views import WeightView

urlpatterns = [
    path('', WeightView.as_view()),
]
