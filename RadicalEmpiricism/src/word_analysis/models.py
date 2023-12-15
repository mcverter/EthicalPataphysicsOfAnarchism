from django.db import models

class Book_Lines(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint("book", "line", name="unique_lower_name_category")]

    book = models.CharField(max_length=3)
    line = models.IntegerField()


class Etymology(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['french_explanation', 'english_explanation'],
                                    name='unique_explanations_ety'),
        ]

    french_explanation  = models.TextField()
    english_explanation  = models.TextField()


class Definition(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['french_explanation', 'english_explanation'],
                                    name='unique_explanations_def'),
        ]

    french_explanation  = models.TextField()
    english_explanation  = models.TextField()


# Create your models here.
class Semantic_Categories(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['french', 'english'], name='unique_fields_sem'),
        ]

    french=  models.CharField(max_length=100, unique=True, null=True)
    english=  models.CharField(max_length=100, unique=True, null=True)
    french_explanation  = models.TextField()
    english_explanation  = models.TextField()

    def __str__(self):
        return self.french


class Etymological_Root(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['root'], name='unique_etymological_root'),
        ]

    root = models.CharField(max_length=32, unique=True, null=True)
    french_explanation  = models.TextField()
    english_explanation  = models.TextField()

    def __str__(self):
        return self.root


class Verb_Type(models.Model):
    french=  models.CharField(max_length=100, unique=True, null=True)
    english=  models.CharField(max_length=100, unique=True, null=True)
    french_explanation  = models.TextField()
    english_explanation  = models.TextField()

    def __str__(self):
        return self.french


class Noun_Type(models.Model):
    french=  models.CharField(max_length=100, unique=True, null=True)
    english=  models.CharField(max_length=100, unique=True, null=True)
    french_explanation  = models.TextField()
    english_explanation  = models.TextField()

    def __str__(self):
        return self.french


class Part_Of_Speech(models.Model):
    french=  models.CharField(max_length=100, unique=True, null=True)
    english=  models.CharField(max_length=100, unique=True, null=True)
    french_explanation  = models.TextField()
    english_explanation  = models.TextField()
    verb_type = models.ForeignKey(Verb_Type, null=True, on_delete=models.SET_NULL)
    noun_type = models.ForeignKey(Noun_Type, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.french


class Suffix(models.Model):
    french=  models.CharField(max_length=100, unique=True, null=True)
    english=  models.CharField(max_length=100, unique=True, null=True)
    french_explanation  = models.TextField()
    english_explanation  = models.TextField()

    def __str__(self):
        return self.french


class Prefix(models.Model):
    french=  models.CharField(max_length=100, unique=True, null=True)
    english=  models.CharField(max_length=100, unique=True, null=True)
    mooface  = models.TextField()
    english_explanation  = models.TextField()

    def __str__(self):
        return self.french


class Word(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['french'], name='unique_original_word'),
        ]

    # word from books
    french = models.CharField(max_length=100, unique=True, null=True)
    english=  models.CharField(max_length=100, unique=True)

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
    book_lines = models.ManyToManyField(Book_Lines)

    def __str__(self):
        return self.french


'''
ERRORS:
word_analysis.Word.book: (models.E006) The field 'book' clashes with the field 'book' from model 'word_analysis.word'.
word_analysis.Word.book: (models.E006) The field 'book' clashes with the field 'book' from model 'word_analysis.word'.
word_analysis.Word.book: (models.E006) The field 'book' clashes with the field 'book' from model 'word_analysis.word'.
word_analysis.Word.book: (models.E006) The field 'book' clashes with the field 'book' from model 'word_analysis.word'.
word_analysis.Word.book: (models.E006) The field 'book' clashes with the field 'book' from model 'word_analysis.word'.
word_analysis.Word.book: (models.E006) The field 'book' clashes with the field 'book' from model 'word_analysis.word'.
word_analysis.Word.line: (models.E006) The field 'line' clashes with the field 'line' from model 'word_analysis.word'.
word_analysis.prefix.french_explanation: (models.E006) The field 'french_explanation' clashes with the field 'french_explanation' from model 'word_analysis.prefix'.
word_analysis.prefix.french_explanation: (models.E006) The field 'french_explanation' clashes with the field 'french_explanation' from model 'word_analysis.prefix'.
word_analysis.prefix.french_explanation: (models.E006) The field 'french_explanation' clashes with the field 'french_explanation' from model 'word_analysis.prefix'.
word_analysis.prefix.french_explanation: (models.E006) The field 'french_explanation' clashes with the field 'french_explanation' from model 'word_analysis.prefix'.
word_analysis.prefix.french_explanation: (models.E006) The field 'french_explanation' clashes with the field 'french_explanation' from model 'word_analysis.prefix'.
word_analysis.prefix.french_explanation: (models.E006) The field 'french_explanation' clashes with the field 'french_explanation' from model 'word_analysis.prefix'.
word_analysis.prefix.french_explanation: (models.E006) The field 'french_explanation' clashes with the field 'french_explanation' from model 'word_analysis.prefix'.
word_analysis.prefix.french_explanation: (models.E006) The field 'french_explanation' clashes with the field 'french_explanation' from model 'word_analysis.prefix'.
word_analysis.prefix.french_explanation: (models.E006) The field 'french_explanation' clashes with the field 'french_explanation' from model 'word_analysis.prefix'.
'''
