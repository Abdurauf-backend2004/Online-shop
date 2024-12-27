from django.db import models

class Mahsulot(models.Model):
    mahsulot_nomi=models.CharField(max_length=255)
    chiqarilgan_sana=models.DateField()
    yaroqlilik_muddati=models.DateField()
    mavjud_miqdori=models.CharField(max_length=255)

    def __str__(self):
        return self.mahsulot_nomi
    class Meta:
        verbose_name_plural='Mahsulotlar'

class Mijoz(models.Model):
    ism=models.CharField(max_length=255)
    familya=models.CharField(max_length=255)
    telefon_raqam=models.CharField(max_length=20)
    manzil=models.CharField(max_length=50)


    def __str__(self):
        return f'{self.ism} {self.familya}'
    class Meta:
        verbose_name_plural='Mijozlar'

class Buyurtma(models.Model):
    mijoz_id=models.ForeignKey(Mijoz,on_delete=models.SET_NULL,null=True)
    mahsulot_id=models.ForeignKey(Mahsulot,on_delete=models.SET_NULL,null=True)
    jami_narx=models.PositiveSmallIntegerField()
    sana=models.DateField()
    status=models.CharField(max_length=50,choices=(('Qabul qilingan','Qabul qilingan'),('Yuborilgan','Yuborilgan'),('Yetkazib berilgan','Yetkazib berilgan')))

    def __str__(self):
        return f'{self.mijoz_id} - {self.mahsulot_id} {self.jami_narx} so`m'

    class Meta:
        verbose_name_plural = 'Buyurtmalar'







