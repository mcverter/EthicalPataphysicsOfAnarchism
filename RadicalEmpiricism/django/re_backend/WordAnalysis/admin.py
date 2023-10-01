from django.contrib import admin

from .models import Word, SemanticCategory, EtymologicalRoot, VerbType, NounType, Suffix, Prefix, PartOfSpeech

# Register your models here
'''
class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
'''

admin.site.register(Word)
admin.site.register(SemanticCategory)
admin.site.register(EtymologicalRoot)
admin.site.register(VerbType)
admin.site.register(NounType)
admin.site.register(Suffix)
admin.site.register(Prefix)
admin.site.register(PartOfSpeech)
