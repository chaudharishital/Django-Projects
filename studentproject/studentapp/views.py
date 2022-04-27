from django.shortcuts import render
from . import forms
# Create your views here.
def studentview(request):
    form=forms.Register()
    if request.method=="POST":
        form=forms.Register(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("data inserted successfully")
            return render(request,'thankyou.html')
    return render(request,'register.html',context={"studentform":form})
