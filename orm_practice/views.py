from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def index(request):
    students=Student.objects.all()
    context={
        'students':students
    }
    return render(request, 'orm_practice/index.html', context)

def detail(request, pk):
    student=Student.objects.get(pk=pk)
    context={
        'student':student
    }
    return render(request, 'orm_practice/detail.html', context)

# Create(생성)
def new(request):
    return render(request, 'orm_practice/new.html')

def create(request):
    # 실제 처리하는 부분
    s=Student()
    s.name=request.GET['name']
    #tmp_age=int(request.GET.get('age'))
    s.age=request.GET.get('age')
    s.major=request.GET.get('major')
    s.intro=request.GET.get('intro')
    s.save()
    #return redirect('index') #새로고침
    return redirect('detail', pk=s.id)