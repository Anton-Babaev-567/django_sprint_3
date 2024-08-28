from django.contrib import admin

# Register your models here.
from .models import Post, Category, Location


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('text',)
    list_display = ('id', 'title', 'author', 'text', 'category',
                    'pub_date', 'location', 'is_published', 'created_at'
                    )
    list_display_links = ('title',)
    list_editable = ('category', 'is_published', 'location',)
    list_filter = ('created_at',)
    empty_value_display = '-пусто-'


admin.site.register(Category)
admin.site.register(Location)
