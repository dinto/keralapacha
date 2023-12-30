from django.db import models


class Product(models.Model):
  name = models.CharField(max_length=250)
  available_Qty = models.IntegerField(blank=True,null=True)
  sold_Qty  = models.IntegerField(blank=True,null=True)
  retail_Price  = models.DecimalField(max_digits=19,decimal_places = 2 ,null=True,blank=True)
  wholesale_price = models.DecimalField(max_digits=19,decimal_places = 2 ,null=True,blank=True)
  validity = models.CharField(max_length=250)
  manufacture_Date= models.DateField(blank=True,null=True)

  def __str__(self):
    return  self.name + '' + str(self.manufacture_Date)

class Customer(models.Model):
  Name = models.CharField(max_length=250)
  Address = models.CharField(max_length=250)
  Pincode  = models.IntegerField(blank=True,null=True)
  LandMark  = models.CharField(max_length=250,blank=True,null=True)
  Phone1 = models.CharField(max_length=250)
  Phone2 = models.CharField(max_length=250,blank=True,null=True)
  Gst_number= models.CharField(max_length=250,blank=True,null=True)

  def __str__(self):
    return  self.Name + '-' + self.Phone1

class Company(models.Model):
  Name = models.CharField(max_length=250)
  Address = models.CharField(max_length=250,blank=True,null=True)
  Pincode  = models.IntegerField(blank=True,null=True)
  LandMark  = models.CharField(max_length=250,blank=True,null=True)
  Phone1 = models.CharField(max_length=250)
  Phone2 = models.CharField(max_length=250,blank=True,null=True)
  Gst_number= models.CharField(max_length=250,blank=True,null=True)

  def __str__(self):
    return  self.Name + '-' + self.Phone1

class Order_Details(models.Model):
  Item = models.CharField(max_length=250)
  Qty=models.IntegerField(blank=True,null=True)
  Price = models.DecimalField(max_digits=19,decimal_places = 2 ,null=True,blank=True)
  Is_whole_price = models.BooleanField()
  Is_discounted = models.BooleanField()
  Discount= models.CharField(max_length=250)
  Price_After_Discount= models.DecimalField(max_digits=19,decimal_places = 2 ,null=True,blank=True)
  Total= models.DecimalField(max_digits=19,decimal_places = 2 ,null=True,blank=True)
  Is_Cash_On_Delivery= models.BooleanField()
  Date= models.DateTimeField(blank=True,null=True)
  Customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='Customer_Details')
  Order_Status= models.CharField(max_length=250)
  Payment_Status= models.CharField(max_length=250)
  def __str__(self):
    return  self.Item + '-' + self.Order_Status

class Salary_Type(models.Model):
  Type= models.CharField(max_length=250)
  
  def __str__(self):
    return  self.Type 


class Labour_Details(models.Model):
  Name = models.CharField(max_length=250)
  Phone = models.CharField(max_length=250)
  Salary_type = models.ForeignKey(Salary_Type,on_delete=models.CASCADE,related_name='Salary_Type')
    
  def __str__(self):
    return  self.Name 

class Labour_Salary(models.Model):
  Date = models.DateField(blank=True,null=True)
  Salary = models.DecimalField(max_digits=19,decimal_places = 2 ,null=True,blank=True)
  Labour_Id= models.ForeignKey(Labour_Details,on_delete=models.CASCADE,related_name='Labour_Details')

  def __str__(self):
    return  str(self.Labour_Id) + '-' + str(self.Date)

class Vehicle_Details(models.Model):
  Vehicle_Number = models.CharField(max_length=250,null=True,blank=True)
  Vehicle_Owner_Name = models.CharField(max_length=250)
  Phone=models.CharField(max_length=250)

  def __str__(self):
    return  self.Vehicle_Owner_Name 

class Vehicle_Cost(models.Model):
  Date = models.DateField(blank=True,null=True)
  Cost = models.DecimalField(max_digits=19,decimal_places = 2 ,null=True,blank=True)
  Distance = models.DecimalField(max_digits=19,decimal_places = 2 ,null=True,blank=True)
  Vehicle_Id= models.ForeignKey(Vehicle_Details,on_delete=models.CASCADE,related_name='Vehicle_Details')

  def __str__(self):
    return  str(self.Date) + '-' + str(self.Vehicle_Id)

class Item_Purchased(models.Model):
  Item  = models.CharField(max_length=250)
  Date  = models.DateField(blank=True,null=True)
  Qty   = models.IntegerField(blank=True,null=True)
  Buying_Price = models.DecimalField(max_digits=19,decimal_places = 2 ,null=True,blank=True)
  Land_Mark = models.CharField(max_length=250,null=True,blank=True)
  Address = models.CharField(max_length=250,null=True,blank=True)
  Phone = models.CharField(max_length=250,null=True,blank=True)
  Labour_Charge = models.DecimalField(max_digits=19,decimal_places = 2 ,null=True,blank=True)
  Final_Price = models.DecimalField(max_digits=19,decimal_places = 2 ,null=True,blank=True)
    
  def __str__(self):
    return  self.Item + '-' + str(self.Date)

