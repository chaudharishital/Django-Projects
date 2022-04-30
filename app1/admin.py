from django.contrib import admin
from app1.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    model=Student
    list_display=['id','name','roll_no','marks']

admin.site.register(Student,StudentAdmin)
