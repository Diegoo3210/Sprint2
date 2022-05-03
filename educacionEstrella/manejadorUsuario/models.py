from django.db import models
# Create your models here. 

class usuarioRegistrado(models.Model):
    name = models.CharField(max_length=40, null = True)
    last_name = models.CharField(max_length=40, null = True)
    address = models.CharField(max_length=20, null = True)
    email = models.EmailField(null = True)
    phone = models.CharField(max_length=20, null = True)
    university = models.CharField(max_length=40, null = True)
    scan_id = models.FileField(upload_to=settings.MEDIA_ROOT, null=True)

    @classmethod
    def create(cls, name, last_name, address, email, phone, university, scan_id):
        usuarioReg = cls(name = name, last_name = last_name, address = address, email = email,
                    phone = phone, university = university, scan_id = scan_id)
        return usuarioReg