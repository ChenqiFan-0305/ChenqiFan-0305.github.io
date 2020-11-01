from django.contrib import admin

# Register your models here.
from .models import Link, Article, Sim_rate, Topic, Source

class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_url',
    'status')
admin.site.register(Link, LinkAdmin)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    pass
    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'scientific_rate' )
    
@admin.register(Sim_rate)
class Sim_rateAdmin(admin.ModelAdmin):
    pass
    

