from django.contrib import admin
from .models import ShopItems,ItemThubnail,ItemThubnailTag
# Register your models here.
admin.site.register(ShopItems)
admin.site.register(ItemThubnail)
admin.site.register(ItemThubnailTag)