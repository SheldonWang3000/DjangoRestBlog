from django.contrib import admin

from .models import (DeleteArray, DeleteTransaction)

admin.site.register(DeleteTransaction)
admin.site.register(DeleteArray)