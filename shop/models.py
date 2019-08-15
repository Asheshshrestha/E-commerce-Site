from django.db import models

# Create your models here.

class Product(models.Model):
    #CHOICES =(("0","Art & Crafts"),("1","Baby"),("2","Beauty & Personal care"),("3","Books"),("4","Computers"),("5","Electronics"),("6","Women's Fashion"),("7","Men's Fashion"),("8","Girl's Fashion"),("9","Boys's Fashion"),("10","Home & Kitchen"),("11","Others"))
    CHOICES =(("Art & Crafts","Art & Crafts"),("Baby","Baby"),("Beauty & Personal care","Beauty & Personal care"),("Books","Books"),("Computers","Computers"),("Electronics","Electronics"),("Women's Fashion","Women's Fashion"),("Men's Fashion","Men's Fashion"),("Girl's Fashion","Girl's Fashion"),("Boys's Fashion","Boys's Fashion"),("Home & Kitchen","Home & Kitchen"),("Others","Others"))
    #CHOICES =("Art & Crafts","Baby","Beauty & Personal care","Books","Computers","Electronics","Women's Fashion","Men's Fashion","Girl's Fashion","Boys's Fashion","Home & Kitchen","Others")

    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CHOICES)
    
    subcategory = models.CharField(max_length=50, default="")
    
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name