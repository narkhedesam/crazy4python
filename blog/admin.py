from django.contrib import admin
from .models import post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


admin.site.register(post, PostAdmin)