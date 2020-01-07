from django.shortcuts import render
from portapp.models import Project

# Create your views here.
def project_index (request):
    projects=Project.objects.all()
    context={
        'projects':projects
    }
    return render (request,'project_index.html',context)
