from django.contrib import admin
from .models import Meeting, MeetingMember

# Register your models here.
@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    pass

@admin.register(MeetingMember)
class MeetingMemberAdmin(admin.ModelAdmin):
    pass
