from django.http import JsonResponse
from django.utils.timezone import now
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Person
from .forms import PersonForm, FeedbackForm



class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'person_form.html'
    success_url = reverse_lazy('person_list')


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'person_form.html'
    success_url = reverse_lazy('person_list')



def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            satisfacao = form.cleaned_data['satisfacao']
            return render(request, 'agradecimento.html', {
                'nome': nome,
                'satisfacao': satisfacao
            })
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})



def welcome_view(request):
    return JsonResponse({"message": "Welcome to the Personal Info API!"})


def goodbye_view(request):
    return JsonResponse({"message": "Goodbye, see you next time!"})


def current_time_view(request):
    current_time = now().strftime("%H:%M:%S")
    return JsonResponse({"current_time": current_time})


def greet_view(request):
    name = request.GET.get('name')
    if name:
        message = f"Hello, {name}!"
    else:
        message = "Hello, Stranger!"
    return JsonResponse({"message": message})


def age_category_view(request):
    age = request.GET.get('age')
    if age is None:
        return JsonResponse({"error": "Missing 'age' parameter."}, status=400)
    try:
        age_int = int(age)
    except ValueError:
        return JsonResponse({"error": "Invalid 'age' parameter, must be an integer."}, status=400)

    if age_int < 0:
        category = "Invalid age"
    elif age_int <= 12:
        category = "Child"
    elif age_int <= 17:
        category = "Teenager"
    elif age_int <= 59:
        category = "Adult"
    else:
        category = "Senior"
    return JsonResponse({"category": category})


def sum_view(request, num1, num2):
    try:
        n1 = int(num1)
        n2 = int(num2)
    except ValueError:
        return JsonResponse({"error": "Invalid input, please provide two integers."})
    return JsonResponse({"sum": n1 + n2})