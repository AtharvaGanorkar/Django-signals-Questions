from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

class AgModel(models.Model):
    name = models.CharField(max_length=100)


@receiver(post_save, sender=AgModel)
def Ag_signal(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(3)  
    print("Signal handler finished")


def test_signal():
    print("Creating AgModel instance")
    AgModel.objects.create(name="Test")
    print("AgModel instance created")


test_signal()