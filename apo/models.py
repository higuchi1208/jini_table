from django.db import models

class Jini(models.Model):
    MSN = models.CharField(verbose_name="電話番号", max_length=20)
    model = models.CharField(verbose_name="機種", max_length=30)
    subtotal = models.IntegerField(verbose_name="小計")
    call = models.CharField(verbose_name="通話", max_length=10)
    GB = models.IntegerField(verbose_name="ネット")
    hs = models.CharField(verbose_name="半サポ", max_length=10)
    suport = models.CharField(verbose_name="割引", max_length=500)


