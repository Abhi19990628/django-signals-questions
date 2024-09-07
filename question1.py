# By default, Django signals execute synchronously. This means the signal handler is executed in the same thread, and the sender waits until the handler completes its execution before proceeding.

# Code Example:
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received for:", instance.name)

# Creating an instance of MyModel
obj = MyModel.objects.create(name="Test")
print("Object created")  # This prints after the signal handler finishes