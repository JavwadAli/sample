from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    param = {'name': 'javwad', 'lname': 'choudhary','n2':'Fahim','l2':'Shaikh'}
    return render(request,'index.html',param)
def table(request):
    return render(request,'table.html')
