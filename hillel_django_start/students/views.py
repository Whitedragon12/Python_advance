from django.http import JsonResponse
from .models import Student, Teacher
from faker import Faker
import random


def generate_student(request):
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    age = random.randint(18, 30)

    student = Student.objects.create(first_name=first_name, last_name=last_name, age=age)
    return JsonResponse({"id": student.id, "first_name": student.first_name, "last_name": student.last_name, "age": student.age})


def generate_students(request):
    count = request.GET.get('count', 10)
    try:
        count = int(count)
        if count < 1 or count > 100:
            raise ValueError()
    except ValueError:
        return JsonResponse({"error": "Invalid 'count' parameter. It should be an integer between 1 and 100."}, status=400)

    students = []
    for _ in range(count):
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        age = random.randint(18, 30)

        student = Student.objects.create(first_name=first_name, last_name=last_name, age=age)
        students.append({"id": student.id, "first_name": student.first_name, "last_name": student.last_name, "age": student.age})

    return JsonResponse(students, safe=False)


def generate_teacher(request):
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    subject = fake.word()

    teacher = Teacher.objects.create(first_name=first_name, last_name=last_name, subject=subject)
    return JsonResponse({"id": teacher.id, "first_name": teacher.first_name, "last_name": teacher.last_name, "subject": teacher.subject})
