# models.py
from django.db import models

class Opening(models.Model):
    name = models.CharField(max_length=255)
    eco = models.CharField(max_length=10, blank=True)
    moves = models.TextField()  # Store the sequence of moves in UCI notation

    def __str__(self):
        return self.name

class Variation(models.Model):
    opening = models.ForeignKey(Opening, on_delete=models.CASCADE, related_name='variations')
    name = models.CharField(max_length=255)
    moves = models.TextField()  # Store the sequence of moves in UCI notation

    def __str__(self):
        return self.name
