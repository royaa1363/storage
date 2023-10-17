from django.db import models


class Primary(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.title}"


class Product(models.Model):
    title = models.CharField(max_length=256)
    pro_num = models.IntegerField(max_length=None)
    pro_date = models.DateField(null=True, blank=True)
    primary = models.ManyToManyField(Primary)

    def __str__(self):
        return f"{self.title}"
