from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TODO(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    is_completed = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class  Meta:
        db_table = 'TODO'
        ordering = ['-updated_date']

    def __str__(self):
        return f'{self.title}'

