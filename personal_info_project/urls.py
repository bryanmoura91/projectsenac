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
]