from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory, Circle, CircleSeries, CircleCategory
from tinymce.widgets import TinyMCE
from django.db import models

class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {"fields": ["tutorial_title", "tutorial_published"]}),
        ("URL", {"fields":["tutorial_slug"]}),
        ("Series", {"fields":["tutorial_series"]}),
        ("Content", {"fields":["tutorial_content"]}),
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

admin.site.register(TutorialSeries)        
admin.site.register(TutorialCategory)        
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(CircleSeries)        
admin.site.register(CircleCategory)        
admin.site.register(Circle)
