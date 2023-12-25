from django.contrib import admin

from .models import Word, Semantic_Categories, Etymological_Root, Verb_Type, Noun_Type, Suffix, Prefix, Part_Of_Speech

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
admin.site.register(Semantic_Categories)
admin.site.register(Etymological_Root)
admin.site.register(Verb_Type)
admin.site.register(Noun_Type)
admin.site.register(Suffix)
admin.site.register(Prefix)
admin.site.register(Part_Of_Speech)
