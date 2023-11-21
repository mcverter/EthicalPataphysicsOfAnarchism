from django.db import models

REQUIRED_CHAR_FIELD = models.CharField(max_length=100, unique=True)
CHAR_FIELD = models.CharField(max_length=100, unique=True, null=True)
TEXT_FIELD = models.TextField()
INTEGER_FIELD = models.IntegerField()


class Etymology(models.Model):
    french_explanation: TEXT_FIELD
    english_explanation: TEXT_FIELD


class Definition(models.Model):
    french_explanation: TEXT_FIELD
    english_explanation: TEXT_FIELD


# Create your models here.
class SemanticCategory(models.Model):
    french: CHAR_FIELD
    english: CHAR_FIELD
    french_explanation: TEXT_FIELD
    english_explanation: TEXT_FIELD

    def __str__(self):
        return self.french


class EtymologicalRoot(models.Model):
    root: models.CharField(max_length=32, unique=True, null=True)
    french_explanation: TEXT_FIELD
    english_explanation: TEXT_FIELD

    def __str__(self):
        return self.root


class VerbType(models.Model):
    french: CHAR_FIELD
    english: CHAR_FIELD
    french_explanation: TEXT_FIELD
    english_explanation: TEXT_FIELD

    def __str__(self):
        return self.french


class NounType(models.Model):
    french: CHAR_FIELD
    english: CHAR_FIELD
    french_explanation: TEXT_FIELD
    english_explanation: TEXT_FIELD

    def __str__(self):
        return self.french


class PartOfSpeech(models.Model):
    french: CHAR_FIELD
    english: CHAR_FIELD
    french_explanation: TEXT_FIELD
    english_explanation: TEXT_FIELD
    verbType: models.ForeignKey(VerbType, on_delete=models.SET_NULL)
    nounType: models.ForeignKey(NounType, on_delete=models.SET_NULL)

    def __str__(self):
        return self.french


class Suffix(models.Model):
    french: CHAR_FIELD
    english: CHAR_FIELD
    french_explanation: TEXT_FIELD
    english_explanation: TEXT_FIELD

    def __str__(self):
        return self.french


class Prefix(models.Model):
    french: CHAR_FIELD
    english: CHAR_FIELD
    french_explanation: TEXT_FIELD
    english_explanation: TEXT_FIELD

    def __str__(self):
        return self.french


class Word(models.Model):
    # word from books
    french: REQUIRED_CHAR_FIELD
    english: CHAR_FIELD

    # count from books
    ti: INTEGER_FIELD
    otb: INTEGER_FIELD

    # etymology and definition
    etymology: models.ForeignKey(Etymology, on_delete=models.SET_NULL)
    definition: models.ForeignKey(Definition, on_delete=models.SET_NULL)

    # connections
    prefix: models.ForeignKey(Prefix, on_delete=models.SET_NULL)
    suffix: models.ForeignKey(Suffix, on_delete=models.SET_NULL)
    partOfSpeech: models.ForeignKey(PartOfSpeech, on_delete=models.SET_NULL)
    etymologicalRoot: models.ForeignKey(EtymologicalRoot, on_delete=models.SET_NULL)
    semanticCategories: models.ManyToManyField(SemanticCategory)

    def __str__(self):
        return self.french
