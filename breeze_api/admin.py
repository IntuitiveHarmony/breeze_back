from django.contrib import admin

# Register your models here.
from .models import Sequence, User
admin.site.register(Sequence)
admin.site.register(User)
