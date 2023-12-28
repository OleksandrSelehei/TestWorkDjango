from django.urls import path
from .views import MethodsViews

urlpatterns = [
    path('', MethodsViews.as_view(), name='display_items'),
]