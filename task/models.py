from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)


class Subcategory(models.Model):
    category = models.CharField(primary_key="task.Category", max_length=140)
    title = models.CharField(max_length=200)


class Advertisement(models.Model):
    title = models.CharField(max_length=240)
    description = models.TextField()
    category = models.ForeignKey("task.Subcategory", on_delete=models.CASCADE)
    created_at = models.DateTimeField()
