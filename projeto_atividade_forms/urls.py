from django.contrib import admin
from django.urls import path
from info_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Parte 1 - rotas simples
    path('welcome', views.welcome_view),
    path('goodbye', views.goodbye_view),
    path('current-time', views.current_time_view),
    path('greet', views.greet_view),
    path('age-category', views.age_category_view),
    path('sum/<str:num1>/<str:num2>', views.sum_view),

    # Parte 2 - rotas para formulário Person
    path('person/create/', views.PersonCreateView.as_view(), name='person_create'),
    path('person/edit/<int:pk>/', views.PersonUpdateView.as_view(), name='person_edit'),

    # Parte 3 - formulário manual de feedback
    path('feedback/', views.feedback_view, name='feedback'),
]
