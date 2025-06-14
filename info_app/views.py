from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse
from datetime import datetime
from .models import Person  # Importa o model Person

class WelcomeView(View):
    def get(self, request):
        return JsonResponse({"message": "Welcome to the Personal Info API!"})

class GoodbyeView(View):
    def get(self, request):
        return JsonResponse({"message": "Goodbye, see you next time!"})

class CurrentTimeView(View):
    def get(self, request):
        now_str = datetime.now().strftime("%H:%M:%S")
        return JsonResponse({"current_time": now_str})

def greet(request):
    name = request.GET.get('name', 'Stranger')
    return JsonResponse({"message": f"Hello, {name}!"})

def age_category(request):
    age = request.GET.get('age')
    if age is None:
        return JsonResponse({"error": "Missing 'age' parameter."}, status=400)
    try:
        age = int(age)
        if age <= 12:
            category = "Child"
        elif age <= 17:
            category = "Teenager"
        elif age <= 59:
            category = "Adult"
        else:
            category = "Senior"
        return JsonResponse({"category": category})
    except ValueError:
        return JsonResponse({"error": "Invalid age parameter."}, status=400)

def sum_numbers(request, num1, num2):
    try:
        total = int(num1) + int(num2)
        return JsonResponse({"sum": total})
    except ValueError:
        return JsonResponse({"error": "Invalid input, please provide two integers."})

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["site_name"] = "Personal Info API"
        context["site_description"] = "Este site fornece informações pessoais através de uma API simples."
        context["current_year"] = datetime.now().year
        return context

class PeopleListView(View):
    def get(self, request):
        people = Person.objects.all().values("name", "age")
        people_list = list(people)
        return JsonResponse(people_list, safe=False)