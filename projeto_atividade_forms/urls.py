from django.contrib import admin
from django.urls import path
from info_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rotas API simples
    path('welcome', views.welcome_view),
    path('goodbye', views.goodbye_view),
    path('current-time', views.current_time_view),
    path('greet', views.greet_view),
    path('age-category', views.age_category_view),
    path('sum/<str:num1>/<str:num2>', views.sum_view),

    # Rotas para formulário Person
    path('person/create/', views.PersonCreateView.as_view(), name='person_create'),
    path('person/edit/<int:pk>/', views.PersonUpdateView.as_view(), name='person_edit'),

    # Rota para listar pessoas com filtro opcional por gênero
    path('person/', views.PersonListView.as_view(), name='person_list'),
]