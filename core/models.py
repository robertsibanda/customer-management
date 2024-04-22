from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    cell = models.CharField(max_length=25)
    national_id = models.CharField(max_length=20)
    dob = models.DateField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + self.last_name
    

    
class Preferences(models.Model):
    receive_news = models.BooleanField(default=True)
    receive_promotions = models.BooleanField(default=True)
    receive_alerts = models.BooleanField(default=True)
    receive_transaction_message = models.BooleanField(default=True)
    receive_pin_change_alert = models.BooleanField(default=True)


    def __str__(self):
        return 'prefences' 


class Account(models.Model):
    account_number = models.BigAutoField(primary_key=True, unique=True)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    preferences = models.ForeignKey(Preferences, on_delete=models.CASCADE)
    branch_code = models.CharField(max_length=230)
    currency = models.CharField(max_length=230)
    pin = models.CharField(max_length=4)
    balance = models.DecimalField(max_digits=50, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.account_number)
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

class Transaction(models.Model):
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='receiver')
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='sender')
    currency = models.CharField(max_length=230)
    amount = models.DecimalField(max_digits=50, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
    




