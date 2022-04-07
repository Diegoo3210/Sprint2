from django.shortcuts import render
from . import models
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, 'formulario.html')

def inicio(request):#Primra vista
    return render(request, 'index.html')
def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.Document(
            title = fileTitle,
            uploadedFile = uploadedFile
        )
        document.save()

    documents = models.Document.objects.all()

    return render(request, "formulario.html", context = {
        "files": documents
    })
    