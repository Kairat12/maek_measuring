
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from profiles.models import Profile


# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'
class UserAdmin(UserAdmin):
    inlines = (ProfileInline,)


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    search_fields = ['lastName', 'givenName', 'patronymicName', 'timesheet_number']



admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)