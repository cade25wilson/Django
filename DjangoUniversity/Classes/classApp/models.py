from django.db import models

class djangoClasses(models.Model):
    Title = models.CharField(max_length=30)
    Course_Number = models.IntegerField()
    Insructor_Name = models.CharField(max_length=60)
    Duration = models.FloatField(default=0.0)

    objects = models.Manager()

    def __str__(self):
        return self.Title


# Create your models here.
