from django.db import models


class Packing1(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.title}"


class Packing2(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.title}"


class Packing3(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.title}"


class Product(models.Model):
    title = models.CharField(max_length=256)
    pro_num = models.IntegerField(max_length=None)
    pro_date = models.DateField(null=True, blank=True)
    packing1 = models.ForeignKey(Packing1, on_delete=models.CASCADE, null=True)
    packing2 = models.ForeignKey(Packing2, on_delete=models.CASCADE, null=True)
    packing3 = models.ForeignKey(Packing3, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title}"
