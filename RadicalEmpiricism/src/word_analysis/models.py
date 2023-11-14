from django.db import models

REQUIRED_CHAR_FIELD = models.CharField(max_length=100, unique=True)
CHAR_FIELD = models.CharField(max_length=100, unique=True, null=True)
TEXT_FIELD = models.TextField()
INTEGER_FIELD = models.IntegerField()

def ForeignKeyModel(fk_model):
    return models.ForeignKey(fk_model, on_delete=models.SET_NULL)

def ManyToManyModel(fk_model):
    return models.ManyToManyField(fk_model)

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
    verbType: ForeignKeyModel(VerbType)
    nounType: ForeignKeyModel(NounType)

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
    etymology: ForeignKeyModel(Etymology)
    definition: ForeignKeyModel(Definition)

    # connections
    prefix: ForeignKeyModel(Prefix)
    suffix: ForeignKeyModel(Suffix)
    partOfSpeech: ForeignKeyModel(PartOfSpeech)
    etymologicalRoot: ForeignKeyModel(EtymologicalRoot)
    semanticCategories: ManyToManyModel(SemanticCategory)

    def __str__(self):
        return self.french
