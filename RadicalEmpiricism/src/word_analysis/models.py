from django.db import models

class Etymology(models.Model):
    french: models.TextField()
    english: models.TextField()

class Definition(models.Model):
    french: models.TextField()
    english: models.TextField()

# Create your models here.
class SemanticCategory(models.Model):
    french: models.CharField(max_length=100, unique=True, null=True)
    english: models.CharField(max_length=100, unique=True, null=True)
    french_explanation: models.TextField()
    english_explanation: models.TextField()

    def __str__(self):
        return self.french


class EtymologicalRoot(models.Model):
    root: models.CharField(max_length=32, unique=True, null=True)
    french_explanation: models.TextField()
    english_explanation: models.TextField()

    def __str__(self):
        return self.french

class VerbType(models.Model):
    french: models.CharField(max_length=100, unique=True, null=True)
    english: models.CharField(max_length=100, unique=True, null=True)
    french_explanation: models.TextField()
    english_explanation: models.TextField()

    def __str__(self):
        return self.french


class NounType(models.Model):
    french: models.CharField(max_length=100, unique=True, null=True)
    english: models.CharField(max_length=100, unique=True, null=True)
    french_explanation: models.TextField()
    english_explanation: models.TextField()

    def __str__(self):
        return self.french

class PartOfSpeech(models.Model):
    french: models.CharField(max_length=100, unique=True, null=True)
    english: models.CharField(max_length=100, unique=True, null=True)
    french_explanation: models.TextField()
    english_explanation: models.TextField()
    verbType: models.ForeignKey(VerbType, on_delete=models.SET_NULL)
    nounType: models.ForeignKey(NounType, on_delete=models.SET_NULL)

    def __str__(self):
        return self.french


class Suffix(models.Model):
    french: models.CharField(max_length=100, unique=True, null=True)
    english: models.CharField(max_length=100, unique=True, null=True)
    french_explanation: models.TextField()
    english_explanation: models.TextField()

    def __str__(self):
        return self.french

class Prefix(models.Model):
    french: models.CharField(max_length=100, unique=True, null=True)
    english: models.CharField(max_length=100, unique=True, null=True)
    french_explanation: models.TextField()
    english_explanation: models.TextField()

    def __str__(self):
        return self.french

class Word(models.Model):
    # word from books
    french: models.CharField(max_length=100, unique=True)
    english: models.CharField(max_length=100, unique=True, null=True)

    # count from books
    ti: models.IntegerField()
    otb: models.IntegerField()

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
