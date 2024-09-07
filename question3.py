# Question 3: Do Django signals run in the same database transaction as the caller?
# Answer:
# Yes, Django signals run in the same database transaction as the caller by default. Any operations performed in the signal handler are part of the same transaction.

# Code Example:
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received for:", instance.name)
    instance.name = "Modified"
    instance.save()

# Creating an instance of MyModel
obj = MyModel.objects.create(name="Original")
print("Name before save:", obj.name)

# Using an explicit transaction
with transaction.atomic():
    obj.name = "Updated"
    obj.save()
    print("Name after save:", obj.name)