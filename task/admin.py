from django.contrib import admin
from task.models import Category, Subcategory, Advertisement


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ["category", "title"]


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "category"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Advertisement, AdvertisementAdmin)
