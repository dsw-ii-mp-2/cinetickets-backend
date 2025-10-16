from django.db import models
from django.core.validators import MinValueValidator
from users.models import User

class Ticket(models.Model):
    bought_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    movie = models.CharField(max_length=50)
    function = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    seat = models.IntegerField()

    def __str__(self):
        return f"{self.movie} - {self.bought_by.email}"
