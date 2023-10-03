from django.db import models


# Create your models here.
class SemanticCategory(models.Model):
    french: models.CharField(max_length=100, unique=True, null=True)
    english: models.CharField(max_length=100, unique=True, null=True)
    french_explanation: models.TextField()
    english_explanation: models.TextField()

    def __str__(self):
        return self.french


class EtymologicalRoot(models.Model):
    french: models.CharField(max_length=32, unique=True, null=True)
    english: models.CharField(max_length=32, unique=True, null=True)
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
    french: models.CharField(max_length=100, unique=True, null=True)
    english: models.CharField(max_length=100, unique=True, null=True)
    french_explanation: models.TextField()
    english_explanation: models.TextField()
    ti: models.IntegerField()
    otb: models.IntegerField()
    prefix: models.ForeignKey(Prefix, on_delete=models.SET_NULL)
    suffix: models.ForeignKey(Suffix, on_delete=models.SET_NULL)
    partOfSpeech: models.ForeignKey(PartOfSpeech, on_delete=models.SET_NULL)
    etymologicalRoot: models.ForeignKey(EtymologicalRoot, on_delete=models.SET_NULL)
    semanticCategories: models.ManyToManyField(SemanticCategory)

    def __str__(self):
        return self.french
