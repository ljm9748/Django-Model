from django.db import models

# Naming Convention => 단일 레코드의 이름(단수형)
class Student(models.Model):
    name= models.CharField(max_length=20)
    age= models.IntegerField()
    major= models.CharField(max_length=100)
    intro = models.TextField()


# CREATE
# 객체 생성하고 s.save()혹은 Student.objects.create(~~~~)
# 가저올때 Student.objects.get(pk=?) 다른조건도 됨(유니크한 경우만)
# Student.objects.all() => 전체 가져오기