from django.shortcuts import render
from  testapp import forms

# Create your views here.

def feedbackinfo(request):
    form=forms.feed()
    return render(request,'testapp/home.html',{'form':form})
