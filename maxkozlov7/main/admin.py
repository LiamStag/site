from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Video, Category

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Video, MyModelAdmin)

admin.site.register(Category, MyModelAdmin)
