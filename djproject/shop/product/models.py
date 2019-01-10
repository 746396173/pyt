from django.db import models

# Create your models here.


class Product(models.Model):
    commodity = (('eat',"零食"),('drink','饮料'),('play','玩具'))

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=True)
    price = models.FloatField()
    category = models.CharField(max_length=128, choices = commodity, default='零食')
    c_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "产品"
        verbose_name_plural = "产品"

