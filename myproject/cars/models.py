from django.db import models


class Marka(models.Model):
    marka_name = models.CharField(max_length=16, unique=True)


    def __str__(self):
        return self.marka_name


class Model(models.Model):
    model_name = models.CharField(max_length=16, unique=True)
    marka_name = models.ForeignKey(Marka, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name


class Cars(models.Model):
        title = models.CharField(max_length=100)
        cars_name = models.CharField(max_length=32)
        description = models.TextField()
        marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        color = models.CharField(max_length=30, blank=True)
        volume = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
        year = models.PositiveIntegerField()
        type_change = models.BooleanField(default=False)
        video = models.FileField(upload_to='vid/', null=True, blank=True)
        image = models.ImageField(upload_to='img/', null=True, blank=True)

        def __str__(self):
            return self.cars_name