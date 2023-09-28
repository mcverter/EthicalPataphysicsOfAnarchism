from django.db import models


# Create your models here.
class SemanticCategory(models.Model):
    text: models.CharField(max_length=100)
    explanation: models.TextField()

    def __str__(self):
        return self.text


class EtymologicalRoot(models.Model):
    text: models.CharField(max_length=32)
    explanation: models.TextField()

    def __str__(self):
        return self.text


class VerbType(models.Model):
    text: models.CharField(max_length=100)
    explanation: models.TextField()

    def __str__(self):
        return self.text


class NounType(models.Model):
    text: models.CharField(max_length=100)
    explanation: models.TextField()

    def __str__(self):
        return self.text


class PartOfSpeech(models.Model):
    text: models.CharField(max_length=100)
    explanation: models.TextField()
    verbType: models.ForeignKey(VerbType)
    nounType: models.ForeignKey(NounType)

    def __str__(self):
        return self.text


class Suffix(models.Model):
    text: models.CharField(max_length=100)
    explanation: models.TextField()

    def __str__(self):
        return self.text


class Prefix(models.Model):
    text: models.CharField(max_length=100)
    explanation: models.TextField()

    def __str__(self):
        return self.text


class Word(models.Model):
    text: models.CharField(max_length=100)
    explanation: models.TextField()

    prefix: models.ForeignKey(Prefix)
    suffix: models.ForeignKey(Suffix)
    partOfSpeech: models.ForeignKey(PartOfSpeech)
    etymologicalRoot: models.ForeignKey(EtymologicalRoot)
    semanticCategories: models.ManyToManyField(SemanticCategory)
