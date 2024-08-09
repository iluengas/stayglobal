from django.contrib import admin
from .models import Category, Product
from django.utils.html import format_html


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


class ProductAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'
    list_display = ('name', 'image_tag', 'category', 'price', 'description')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'name')
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'description', 'price', 'image')
        }),
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
