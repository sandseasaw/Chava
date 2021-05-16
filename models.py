from django.db import models
   
class Product(models.Model):
    name=models.CharField(max_length=40)
    price=models.DecimalField(null=True, max_digits=10, decimal_places=2)
    type0=models.CharField(max_length=20)
    size0=models.CharField(max_length=30)
    desc0=models.CharField(max_length=200, null=True)
    image=models.ImageField(default='default.png', blank=True)
    def __str__(self):
        return "product_id: %s, nameproduct:%s desc0:%s type0:%s size0:%s price0:%s"\
            %(self.id,self.name,self.desc0,self.type0,self.size0,self.price)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('product', args=[str(self.id)])









