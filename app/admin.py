from django.contrib import admin
from .models import Client, Question, Book, Donation
# Register your models here.


admin.site.register(Client)
admin.site.register(Question)
admin.site.register(Book)
admin.site.register(Donation)