from django.shortcuts import render
from . import models
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.template.loader import get_template


def index(request):
    return render(request, 'formulario.html')

ipValidas = ['127.']
def inicio(request):#Primra vista
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
        
    if (ip not in ipValidas):
            
            print("llego") 
            htmly = get_template('Email.html')
            subject, from_email, to = 'welcome', 'educacionestrellafake@gmail.com','thalassamania@gmail.com'
            html_content = htmly.render()
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return render(request, 'formulario.html')

    return render(request, 'index.html'
    )
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
    