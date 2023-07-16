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

class Seat(models.Model):
    seat_no = models.CharField(max_length=255)
    is_booked = models.BooleanField(default=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    occupant_name = models.CharField(max_length=255, null=True, blank=True)
    occupant_email = models.EmailField(null=True, blank=True)
    purchase_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.seat_no