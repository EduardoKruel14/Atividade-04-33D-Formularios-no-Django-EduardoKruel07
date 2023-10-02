from django.db import models

# Create your models here.

class TopMovies(models.Model):
  title= models.CharField(max_length=50)
  director= models.CharField(max_length=70)
  genre=models.CharField(max_length=20)
  release_date=models.DateField()

class MoviesILike(models.Model):
  OPTIONS= [
    ("O", "Once a year"),
    ("T", "Twice a year"),
    ("M", "Three or more times a year")
  ]

  CATEGORY=[
    ("O", "Oscar nominated/winner"),
    ("T", "Thrilling"),
    ("S", "Serious")
  ]
  title=models.CharField(max_length=50)
  how_often=models.CharField(max_length=1, choices=OPTIONS)
  category=models.CharField(max_length=1, choices=CATEGORY)
  

