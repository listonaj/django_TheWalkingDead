from tabnanny import verbose
from django.db import models

# Create a class Topic that inherit from Model (parent class included in Django).
class Topic(models.Model):
    """A topic the user is learning about."""
    # two attributes: txt and date
    # the text is of CharField attribute - character attributes (
    # used for small amount of character : 200 characters)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def _str__(self):
        """Return a tring representation of the model"""
        return self.text

# the class Entry inherit from Django base's Model class
class Entry(models.Model):
    """something specific you know about a topic"""
    # Foreignkey is a data base term : reference to another record in the data base
    # it connects each entry to a specific topic - it is the topic id 
    # <on_delete> tells django that if we delete one topic - every entry associated 
    # with that topic should be deleted too(cascading delete)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    # no size limit for that field
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    #the Meta class has extra info to manage the model
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """return a string representation of the model"""
        # preview the first 50 characters of the entry
        return f"self.txt[:50]"