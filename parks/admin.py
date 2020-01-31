from django.contrib import admin
from .models import Park
from .models import Comment

# Register your models here.
admin.site.register(Park)
admin.site.register(Comment)
