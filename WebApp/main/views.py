from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Country


class MethodsViews(View):

    def get(self, request):
        path = request.path
        if path == '/':
            return self.display_country()
        else:
            return HttpResponse('<h1>Page not found</h1>', status=404)

    def display_country(self):
        countries = Country.objects.all()
        return render(self.request, 'main/countries_list.html', {'countries': countries})
