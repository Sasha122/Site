from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Articles(models.Model):
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    title = models.CharField(max_length = 120)
    post  = models.TextField()
    date  = models.DateTimeField()

    def __str__(self):
        return self.title
