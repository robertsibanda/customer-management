from django.contrib import admin
from .models import PersonalInfo, Account, Transaction, Preferences

# Register your models here.

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'cell', 'national_id', 'dob', 'address')

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'branch_code', 'currency', 'balance', 'date_created')
 

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'receiver', 'sender', 'currency', 'amount', 'date')
    readonly_fields = ('id', 'date')

@admin.register(Preferences)
class PreferencesAdmin(admin.ModelAdmin):
    list_display = ('receive_news', 'receive_promotions', 'receive_alerts', 'receive_transaction_message', 'receive_pin_change_alert')
