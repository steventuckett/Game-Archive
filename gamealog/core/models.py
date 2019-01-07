from django.db import models


# Create your models here.
class Console(models.Model):
    name = models.CharField(max_length=60)
    controllers = models.IntegerField()
    media_type = models.CharField(max_length=60)
    memory_type = models.CharField(max_length=60)
    objects = models.Manager()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=60)
    category = models.CharField(max_length=60)
    beat = models.BooleanField()
    complete = models.BooleanField()
    start_date = models.DateTimeField()
    completion_date = models.DateTimeField(null=True, blank=True)
    console = models.ForeignKey(Console, on_delete=models.CASCADE)
    objects = models.Manager()
    
    #def __str__(self):
        #return "Title - " + self.title + ", Category - " + self.category
