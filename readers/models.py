from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # on delete cascade is automatically handled
    liked_books = models.ManyToManyField(Book, related_name='liked_by_users')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)