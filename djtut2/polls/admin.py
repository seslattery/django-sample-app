from djtut2.polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date information',{'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    list_display = ('question', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    search_fields = ['question']

admin.site.register(Poll, PollAdmin)