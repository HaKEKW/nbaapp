from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default='logo.png', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def get_absolute_url(self):
        return reverse('customer_info_url', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Good(models.Model):
    CATEGORY = (
        ('Jersey', 'Jersey'),
        ('Cap', 'Cap'),
        ('Shorts', 'Shorts'),
        ('Tickets', 'Tickets'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.TextField(max_length=255, null=True, blank=True)
    good_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('good_detail_url', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('good_update_url', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('good_delete_url', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['category']


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out of delivery', 'Out of delivery'),
        ('Delivered', 'Delivered'),
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Good, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f'{self.customer} ordered {self.product}'

    def get_absolute_url(self):
        return reverse('order_detail_url', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('order_update_url', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('order_delete_url', kwargs={'pk': self.pk})