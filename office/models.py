from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Appointee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    designation = models.CharField(max_length=200, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    responsibility = models.TextField(blank=True)
    photo = models.ImageField(upload_to='office/images', blank=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    appointment_date = models.DateField()
    attending = models.BooleanField(default=True)
    appointee = models.ForeignKey(Appointee, on_delete=models.DO_NOTHING, related_name='appointee', blank=True,
                                  null=True)

    class Meta:
        ordering = ('-start_time',)

    def __str__(self):
        return self.title




#install pillow to use image using pip install pillow