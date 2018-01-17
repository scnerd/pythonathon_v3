from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Competition)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Solution)
admin.site.register(File)
