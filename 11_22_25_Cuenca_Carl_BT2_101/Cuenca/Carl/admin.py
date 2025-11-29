from django.contrib import admin
from .models import childClass, parentClass, schoolClass
# Register your models here.

@admin.register(parentClass)
class DataClassChild(admin.ModelAdmin):
    list_display = ('name','parent')
    search_fields = ('name',)

@admin.register(childClass)
class ParentDataClass(admin.ModelAdmin):
    list_display = ('nameChild','relationshipData')
    search_fields = ('nameChild',)

@admin.register(schoolClass)
class SchoolDataClass(admin.ModelAdmin):
    list_display = ('nameChild', 'school')
    search_fields = ('nameChild',)