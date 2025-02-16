from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time


class AGModel(models.Model):
    name = models.CharField(max_length=100)


@receiver(post_save, sender=AGModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(8)  
    print("Signal handler finished")

def test_signal():
    print("Creating AGModel instance...")
    AGModel.objects.create(name="Test")
    print("AGModel instance created")


test_signal()