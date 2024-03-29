from django.db import models


class Book_Line(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint("book", "line", name="unique_lower_name_category")]

    book = models.CharField(max_length=3)
    line = models.IntegerField()
    french = models.TextField(null=True)
    english = models.TextField(null=True)


class Etymology(models.Model):
    french_explanation = models.TextField(null=True)
    english_explanation = models.TextField(null=True)


class Definition(models.Model):
    french_explanation = models.TextField(null=True)
    english_explanation = models.TextField(null=True)


# Create your models here.
class Semantic_Categories(models.Model):
    french = models.CharField(max_length=100, null=True)
    english = models.CharField(max_length=100, null=True)
    french_explanation = models.TextField(null=True)
    english_explanation = models.TextField(null=True)

    def __str__(self):
        return self.french


class Etymological_Root(models.Model):
    root = models.CharField(max_length=32, unique=True, null=True)
    french_explanation = models.TextField(null=True)
    english_explanation = models.TextField(null=True)

    def __str__(self):
        return self.root


class Verb_Type(models.Model):
    french = models.CharField(max_length=100, unique=True, null=True)

    english = models.CharField(max_length=100, unique=True, null=True)
    french_explanation = models.TextField(null=True)
    english_explanation = models.TextField(null=True)

    def __str__(self):
        return self.french


class Noun_Type(models.Model):
    french = models.CharField(max_length=100, unique=True, null=True)
    english = models.CharField(max_length=100, unique=True, null=True)
    french_explanation = models.TextField(null=True)
    english_explanation = models.TextField(null=True)

    def __str__(self):
        return self.french


class Part_Of_Speech(models.Model):
    french = models.CharField(max_length=100, unique=True, null=True)
    english = models.CharField(max_length=100, unique=True, null=True)
    french_explanation = models.TextField(null=True)
    english_explanation = models.TextField(null=True)
    verb_type = models.ForeignKey(Verb_Type, null=True, on_delete=models.SET_NULL)
    noun_type = models.ForeignKey(Noun_Type, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.french


class Suffix(models.Model):
    french = models.CharField(max_length=100, unique=True, null=True)

    english = models.CharField(max_length=100, unique=True, null=True)
    french_explanation = models.TextField(null=True)
    english_explanation = models.TextField(null=True)

    def __str__(self):
        return self.french


class Prefix(models.Model):
    french = models.CharField(max_length=100, unique=True, null=True)
    english = models.CharField(max_length=100, unique=True, null=True)
    french_explanation = models.TextField(null=True)
    english_explanation = models.TextField(null=True)

    def __str__(self):
        return self.french


class Word(models.Model):
    # word from books
    french = models.CharField(max_length=100, unique=True)
    english = models.CharField(max_length=100, null=True)

    # count from books
    ti = models.IntegerField()
    otb = models.IntegerField()

    # etymology and definition
    etymology = models.ForeignKey(Etymology, null=True, on_delete=models.SET_NULL)
    definition = models.ForeignKey(Definition, null=True, on_delete=models.SET_NULL)

    # connections
    prefix = models.ForeignKey(Prefix, null=True, on_delete=models.SET_NULL)
    suffix = models.ForeignKey(Suffix, null=True, on_delete=models.SET_NULL)
    part_of_speech: models.ForeignKey(Part_Of_Speech, null=True, on_delete=models.SET_NULL)
    etymological_root = models.ForeignKey(Etymological_Root, null=True, on_delete=models.SET_NULL)
    semantic_categories = models.ManyToManyField(Semantic_Categories)
    book_line = models.ManyToManyField(Book_Line)

    def __str__(self):
        return self.french
