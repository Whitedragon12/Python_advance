from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('generate-student/', views.generate_student, name='generate_student'),
    path('generate-students/', views.generate_students, name='generate_students'),
    path('generate-teacher/', views.generate_teacher, name='generate_teacher'),
    # Add other URL patterns as needed
]
