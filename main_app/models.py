from django.db import models
import uuid

# Create your models here.
class Customer(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    full_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=250, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name
    
    class Meta:
        ordering = ('-created',)

class Purchase(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=250)
    item_qnty = models.IntegerField()
    item_price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.customer}'

    