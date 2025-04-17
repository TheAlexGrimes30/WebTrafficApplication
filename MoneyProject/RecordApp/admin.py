from django.contrib import admin

from RecordApp.models import Status, TransactionType, Category, SubCategory

admin.site.register(Status)
admin.site.register(TransactionType)
admin.site.register(Category)
admin.site.register(SubCategory)


