from django.contrib import admin
from write.models import MyModel

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("fullname", "lastname", "age",)

admin.site.register(MyModel, MemberAdmin)
