from django.contrib import admin
from catfacts.models import Email_User, Phone_User, Fact

admin.site.register(Email_User)
admin.site.register(Phone_User)
admin.site.register(Fact)