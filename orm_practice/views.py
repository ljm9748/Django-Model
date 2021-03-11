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

# 원래는 post로 처리해야하지만 get으로하는것도 남기기위해 create는 보존
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

def edit(request, pk):
    student=Student.objects.get(pk=pk)
    context={'student':student}
    return render(request, 'orm_practice/edit.html',context)

def update(request, pk):
    if request.method == 'POST':
        student=Student.objects.get(pk=pk)
        # 실제 처리하는 부분
        student.name=request.POST['name']
        student.age=request.POST.get('age')
        student.major=request.POST.get('major')
        student.intro=request.POST.get('intro')
        student.save()
        return redirect('detail', pk=student.id)
    return redirect('edit', pk=pk)

def delete(request, pk):
    if request.method == 'POST':
        student=Student.objects.get(pk=pk)
        student.delete()
        return redirect('index')
    return redirect('detail', pk=pk)