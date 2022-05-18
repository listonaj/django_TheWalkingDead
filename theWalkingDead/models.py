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