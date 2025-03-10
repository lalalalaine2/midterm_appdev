from django.db import models
from datetime import date

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    
    STATUS_CHOICES = [
        ('Overdue', 'Overdue'),
        ('Due Today', 'Due Today'),
        ('Upcoming', 'Upcoming'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Upcoming')

    def save(self, *args, **kwargs):
        if self.due_date < date.today():
            self.status = 'Overdue'
        elif self.due_date == date.today():
            self.status = 'Due Today'
        else:
            self.status = 'Upcoming'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
