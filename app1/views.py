from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
# Create your views here.
def getdata(request,pk):
    studentobj=Student.objects.get(id=pk)
    print(studentobj)
    #convert queryset(complex datatype) to python dict
    student_dict=StudentSerializer(studentobj)
    print(student_dict)
    #convert python dict to JSON using JSONRenderer
    student_json=JSONRenderer().render(student_dict.data)
    print(student_json)
    return HttpResponse(student_json,content_type='application/json')
