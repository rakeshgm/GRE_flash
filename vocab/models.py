from django.db import models
# Create your models here.


class Word_List(models.Model):
    name = models.CharField(max_length= 25)

    def __unicode__(self):
        return  self.name


class Word(models.Model):

    word_list = models.ForeignKey(Word_List)
    word = models.CharField(max_length=45)
    meaning = models.CharField(max_length= 100 )

    example = models.TextField(max_length= 500)


    def __unicode__(self):

        return self.word

