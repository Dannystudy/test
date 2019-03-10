from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Student
from .forms import StudentFrom

# Create your views here.
def index(request):
    students = Student.get_all()
    if request.method == 'POST':
        form = StudentFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentFrom()

    context = {
        'students':students,
        'form':form,
    }
    return render(request, 'index.html', context=context)
