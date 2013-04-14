from django.db import models

class Idea(models.Model):
    idea_title = models.CharField(max_length=100)
    idea_text = models.CharField(max_length=500)
    idea_created = models.DateTimeField()
    idea_last_activity = models.DateTimeField()
    
    def __unicode__(self):
        return self.idea_title

class Comment(models.Model):
    comment_text = models.CharField(max_length=500)
    comment_agree = models.IntegerField()
    idea = models.ForeignKey(Idea)
    
    def __unicode__(self):
        return self.comment_text
