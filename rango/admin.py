from django.contrib import admin
from rango.models import Category, Page
# Register your models here.

# create an admin class to define what of the model to display
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    # prepopulated_fields = {'slug':('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)