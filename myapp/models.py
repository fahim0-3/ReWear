from django.db import models
from django_otp.forms import OTPAuthenticationForm
 

# Create your models here.

class user(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=10)
    otp=models.IntegerField(blank=True,null=True)

    def __str__(self) -> str:
        return self.email







class branding(models.Model):
    
    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class prize(models.Model):

    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class color(models.Model):

    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class size(models.Model):

    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    


class main_category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    

class product(models.Model):
    main_category = models.ForeignKey(main_category, on_delete=models.CASCADE, blank=True, null=True)
    branding_id = models.ForeignKey(branding, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to="image", blank=True, null=True)
    img1 = models.ImageField(upload_to="image", blank=True, null=True)
    img2 = models.ImageField(upload_to="image", blank=True, null=True)
    img3 = models.ImageField(upload_to="image", blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    

class add_to_cart(models.Model):
    product_id = models.ForeignKey(product,on_delete=models.CASCADE,blank=True,null=True)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE,blank=True,null=True)
    img=models.ImageField(upload_to="image")
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    qty=models.IntegerField()    
    total=models.IntegerField()

    def __str__(self) -> str:
        return self.name

class coupon(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class billing(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    address = models.CharField(max_length=50) 
    address1 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()
    phone = models.CharField(max_length=15) 
    email = models.EmailField()
    notes = models.TextField()  
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class wishlist(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE,default=1)
    product_id=models.ForeignKey(product,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField()
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    
    def _str_(self):
        return self.name  