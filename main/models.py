from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    poster_url = models.URLField()
    age_rating = models.IntegerField()
    ticket_price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.title