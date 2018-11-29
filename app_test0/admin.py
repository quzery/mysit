from django.contrib import admin

# Register your models here.
from app_test0.models import Character,Contact,Tag
#register your models here
class TagInline(admin.TabularInline):
    model = Tag
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')  #list
    search_fields = ('name',)
    inlines = [TagInline]
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email',),
        }],
        ['Advance', {
            'classes': ('collapse',), #css
            'fields': ('age',),
        }]
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Character])