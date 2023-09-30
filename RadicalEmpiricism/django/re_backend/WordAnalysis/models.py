from django.db import models


# Create your models here.
class SemanticCategory(models.Model):
    french: models.CharField(max_length=100)
    english: models.CharField(max_length=100)
    french_explanation: models.TextField()
    english_explanation: models.TextField()

    def __str__(self):
        return self.french


class EtymologicalRoot(models.Model):
    french: models.CharField(max_length=32)
    english: models.CharField(max_length=32)
    french_explanation: models.TextField()
    english_explanation: models.TextField()

    def __str__(self):
        return self.french

class VerbType(models.Model):
    french: models.CharField(max_length=100)
    english: models.CharField(max_length=100)
    french_explanation: models.TextField()
    english_explanation: models.TextField()

    def __str__(self):
        return self.french


class NounType(models.Model):
    french: models.CharField(max_length=100)
    english: models.CharField(max_length=100)
    french_explanation: models.TextField()
    english_explanation: models.TextField()

    def __str__(self):
        return self.french

class PartOfSpeech(models.Model):
    french: models.CharField(max_length=100)
    english: models.CharField(max_length=100)
    french_explanation: models.TextField()
    english_explanation: models.TextField()
    verbType: models.ForeignKey(VerbType)
    nounType: models.ForeignKey(NounType)

    def __str__(self):
        return self.french


class Suffix(models.Model):
    french: models.CharField(max_length=100)
    english: models.CharField(max_length=100)
    french_explanation: models.TextField()
    english_explanation: models.TextField()

    def __str__(self):
        return self.french

class Prefix(models.Model):
    french: models.CharField(max_length=100)
    english: models.CharField(max_length=100)
    french_explanation: models.TextField()
    english_explanation: models.TextField()

    def __str__(self):
        return self.french

class Word(models.Model):
    french: models.CharField(max_length=100)
    english: models.CharField(max_length=100)
    french_explanation: models.TextField()
    english_explanation: models.TextField()
    ti: models.IntegerField()
    otb: models.IntegerField()
    prefix: models.ForeignKey(Prefix)
    suffix: models.ForeignKey(Suffix)
    partOfSpeech: models.ForeignKey(PartOfSpeech)
    etymologicalRoot: models.ForeignKey(EtymologicalRoot)
    semanticCategories: models.ManyToManyField(SemanticCategory)

    def __str__(self):
        return self.french
