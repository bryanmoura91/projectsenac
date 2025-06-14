from django.contrib import admin
from django.urls import path
from info_app.views import (
    WelcomeView, GoodbyeView, CurrentTimeView,
    greet, age_category, sum_numbers, AboutView,
    PeopleListView  # Importa a view da lista de pessoas
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', WelcomeView.as_view()),
    path('goodbye/', GoodbyeView.as_view()),
    path('current-time/', CurrentTimeView.as_view()),
    path('greet/', greet),
    path('age-category/', age_category),
    path('sum/<int:num1>/<int:num2>/', sum_numbers),
    path('about/', AboutView.as_view()),
    path('people/', PeopleListView.as_view()),  # Rota para listar pessoas em JSON
]