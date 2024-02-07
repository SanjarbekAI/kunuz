from django.contrib import admin
from .models import News,Category,Contact,Comment

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['name','category','upload_time','status']
    list_filter = ['status', 'created_time','category','upload_time']
    search_fields = ['name','text']
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_time'
    ordering = ['status', 'upload_time','name']
    
    


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    
    
admin.site.register(Contact)


@admin.register(Comment)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['user','news','upload_time','active']
    list_filter = ['active', 'upload_time']
    search_fields = ['user','body']
    date_hierarchy = 'upload_time'
    ordering = ['user', 'news','upload_time']
    actions = ['activate_comments','disable_comments']
    
    def activate_comments(self, request,queryset):
        queryset.update(active=True)
        
    def disable_comments(self, request,queryset):
        queryset.update(active=False)