from django.contrib import admin

# Register your models here.

from .models import BookInfo,RoleInfo

class RoleInfoAdmin(admin.ModelAdmin):
    list_display = ["id","rname","rgender","rcontent",]
    list_per_page = 3
    list_filter = ["rgender",]
    search_fields = ["rcontent"]

class RoleInfoInline(admin.StackedInline):
    model = RoleInfo
    extra = 1

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["id","btitle","bpub_data",]
    list_per_page = 3
    inlines = [RoleInfoInline,]

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(RoleInfo,RoleInfoAdmin)