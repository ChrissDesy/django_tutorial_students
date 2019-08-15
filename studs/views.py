from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Student

def index(request):
    latest_students_list = Student.objects.order_by('-saved_date')[:5]
    print(latest_students_list)
    context = {
        'latest_list': latest_students_list
    }
    return render(request, 'studs/index.html', context)

def details(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    return render(request, 'studs/detail.html', {'data': student})

