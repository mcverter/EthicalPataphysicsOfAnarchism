from django.db import migrations, models

ID_FIELD = ('id', models.AutoField(auto_created=True,
                                   primary_key=True,
                                   serialize=True,
                                   verbose_name='ID'))

FRENCH_WORD_COL = ('french', models.CharField(max_length=100, null=True, unique=True))
ENGLISH_WORD_COL = ('english', models.CharField(max_length=100, null=True))
FRENCH_EXPLANATION_COL = ('french_explanation', models.TextField(null=True, unique=True))
ENGLISH_EXPLANATION_COL = ('english_explanation', models.TextField(null=True, unique=True))
BOOK_NAME_COL = ('book', models.CharField(max_length=3))
LINES_COL = ('lines', models.IntegerField())

class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]
    operations = [
        migrations.CreateModel(name='Etymology',
                               fields=[ID_FIELD,
                                       FRENCH_EXPLANATION_COL,
                                       ENGLISH_EXPLANATION_COL]),
        migrations.CreateModel(name='Definition',
                               fields=[ID_FIELD,
                                       FRENCH_EXPLANATION_COL,
                                       ENGLISH_EXPLANATION_COL]),
        migrations.CreateModel(name='Semantic_Category',
                               fields=[ID_FIELD,
                                       FRENCH_WORD_COL,
                                       ENGLISH_WORD_COL,
                                       FRENCH_EXPLANATION_COL,
                                       ENGLISH_EXPLANATION_COL]),
        migrations.CreateModel(name='Etymological_Root',
                               fields=[ID_FIELD,
                                       ('root', models.CharField(max_length=100, null=True, unique=True)),
                                       FRENCH_EXPLANATION_COL,
                                       ENGLISH_EXPLANATION_COL
                                       ]),
        migrations.CreateModel(name='Verb_Type',
                               fields=[ID_FIELD,
                                       FRENCH_WORD_COL,
                                       ENGLISH_WORD_COL,
                                       FRENCH_EXPLANATION_COL,
                                       ENGLISH_EXPLANATION_COL]),
        migrations.CreateModel(name='Noun_Type',
                               fields=[ID_FIELD,
                                       FRENCH_WORD_COL,
                                       ENGLISH_WORD_COL,
                                       FRENCH_EXPLANATION_COL,
                                       ENGLISH_EXPLANATION_COL]),
        migrations.CreateModel(name='Part_Of_Speech',
                               fields=[ID_FIELD,
                                       FRENCH_WORD_COL,
                                       ENGLISH_WORD_COL,
                                       FRENCH_EXPLANATION_COL,
                                       ENGLISH_EXPLANATION_COL,
                                       ('verb_type',
                                        models.ForeignKey(null=True, related_name='verb_type',
                                                          on_delete=models.SET_NULL,
                                                          to='word_analysis.verb_type')),
                                       ('noun_type',
                                        models.ForeignKey(null=True, related_name='noun_type',
                                                          on_delete=models.SET_NULL,
                                                          to='word_analysis.noun_type')),
                                       ]),
        migrations.CreateModel(name='Suffix',
                               fields=[ID_FIELD,
                                       FRENCH_WORD_COL,
                                       ENGLISH_WORD_COL,
                                       FRENCH_EXPLANATION_COL,
                                       ENGLISH_EXPLANATION_COL]),
        migrations.CreateModel(name='Prefix',
                               fields=[ID_FIELD,
                                       FRENCH_WORD_COL,
                                       ENGLISH_WORD_COL,
                                       FRENCH_EXPLANATION_COL,
                                       ENGLISH_EXPLANATION_COL]),
        migrations.CreateModel('Book_Lines',
                               fields=[
                                   ID_FIELD,
                                   BOOK_NAME_COL,
                                   LINES_COL
                               ]),

        migrations.CreateModel(name='Word',
                               fields=[ID_FIELD,
                                       FRENCH_WORD_COL,
                                       ENGLISH_WORD_COL,
                                       ('ti', models.IntegerField()),
                                       ('otb', models.IntegerField()),
                                       ('definition',
                                        models.ForeignKey(null=True, related_name='definition',
                                                          on_delete=models.SET_NULL,
                                                          to='word_analysis.definition')),
                                       ('etymology',
                                        models.ForeignKey(null=True, related_name='etymology',
                                                          on_delete=models.SET_NULL,
                                                          to='word_analysis.etymology')),
                                       ('prefix',
                                        models.ForeignKey(null=True, related_name='prefix',
                                                          on_delete=models.SET_NULL,
                                                          to='word_analysis.prefix')),
                                       ('suffix',
                                        models.ForeignKey(related_name='suffix',
                                                          on_delete=models.SET_NULL,
                                                          to='word_analysis.suffix', null=True, blank=True,)),
                                       ('part_of_speech',
                                        models.ForeignKey(null=True, related_name='part_of_speech',
                                                          on_delete=models.SET_NULL,
                                                          to='word_analysis.part_of_speech')),
                                       ('etymological_root',
                                        models.ForeignKey(null=True, related_name='etymological_root',
                                                          on_delete=models.SET_NULL,
                                                          to='word_analysis.etymological_root')),
                                       ('semantic_categories',
                                        models.ManyToManyField(to='word_analysis.semantic_category')),
                                       ('book_lines',
                                        models.ManyToManyField(to='word_analysis.book_lines')),
                            
                                       ],
                               )
    ]
