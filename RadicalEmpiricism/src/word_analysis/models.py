from django.db import models

REQUIRED_CHAR_FIELD = models.CharField(max_length=100, unique=True)
CHAR_FIELD = models.CharField(max_length=100, unique=True, null=True)
TEXT_FIELD = models.TextField()
INTEGER_FIELD = models.IntegerField()

class Book_Lines(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint("book", "line", name="unique_lower_name_category")]
    book = CHAR_FIELD
    line = INTEGER_FIELD

class Etymology(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['french_explanation', 'english_explanation'], name='unique_explanations_ety'),
        ]
    french_explanation = TEXT_FIELD
    english_explanation = TEXT_FIELD


class Definition(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['french_explanation', 'english_explanation'], name='unique_explanations_def'),
        ]
    french_explanation = TEXT_FIELD
    english_explanation = TEXT_FIELD


# Create your models here.
class Semantic_Categories(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['french', 'english'], name='unique_fields_sem'),
        ]
    french = CHAR_FIELD
    english = CHAR_FIELD
    french_explanation = TEXT_FIELD
    english_explanation = TEXT_FIELD

    def __str__(self):
        return self.french


class Etymological_Root(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['root'], name='unique_etymological_root'),
        ]
    root = models.CharField(max_length=32, unique=True, null=True)
    french_explanation = TEXT_FIELD
    english_explanation = TEXT_FIELD

    def __str__(self):
        return self.root


class Verb_Type(models.Model):
    french = CHAR_FIELD
    english = CHAR_FIELD
    french_explanation = TEXT_FIELD
    english_explanation = TEXT_FIELD

    def __str__(self):
        return self.french


class Noun_Type(models.Model):
    french = CHAR_FIELD
    english = CHAR_FIELD
    french_explanation = TEXT_FIELD
    english_explanation = TEXT_FIELD

    def __str__(self):
        return self.french


class Part_Of_Speech(models.Model):
    french = CHAR_FIELD
    english = CHAR_FIELD
    french_explanation = TEXT_FIELD
    english_explanation = TEXT_FIELD
    verb_type = models.ForeignKey(Verb_Type, on_delete=models.SET_NULL)
    noun_type = models.ForeignKey(Noun_Type, on_delete=models.SET_NULL)

    def __str__(self):
        return self.french


class Suffix(models.Model):
    french = CHAR_FIELD
    english = CHAR_FIELD
    french_explanation = TEXT_FIELD
    english_explanation = TEXT_FIELD

    def __str__(self):
        return self.french


class Prefix(models.Model):
    french = CHAR_FIELD
    english = CHAR_FIELD
    french_explanation = TEXT_FIELD
    english_explanation = TEXT_FIELD

    def __str__(self):
        return self.french


class Word(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['french'], name='unique_original_word'),
        ]

    # word from books
    french = REQUIRED_CHAR_FIELD
    english = CHAR_FIELD

    # count from books
    ti = INTEGER_FIELD
    otb = INTEGER_FIELD

    # etymology and definition
    etymology = models.ForeignKey(Etymology, on_delete=models.SET_NULL)
    definition = models.ForeignKey(Definition, on_delete=models.SET_NULL)

    # connections
    prefix = models.ForeignKey(Prefix, on_delete=models.SET_NULL)
    suffix = models.ForeignKey(Suffix, on_delete=models.SET_NULL)
    part_of_speech: models.ForeignKey(Part_Of_Speech, on_delete=models.SET_NULL)
    etymological_root = models.ForeignKey(Etymological_Root, on_delete=models.SET_NULL)
    semantic_categories = models.ManyToManyField(Semantic_Categories)
    book_lines = models.ManyToManyField(Book_Lines)

    def __str__(self):
        return self.french
