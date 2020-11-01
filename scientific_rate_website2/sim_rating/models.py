from django.db import models
import uuid

# Create your models here.
class Link(models.Model):
    """
    Model representing the article link
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular article in the database")
    external_url = models.URLField()
    
    PROCESS_STATUS = (
        ('u', 'unprocessed'),
        ('p', 'processed without scientific rate'),
        ('s', 'processed with a scientific rate'),
    )
    
    status = models.CharField(max_length=1, choices=PROCESS_STATUS, blank=True, default='u', help_text='Whether the link is stored as a processed article')

    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.external_url
        
class Topic(models.Model):
    """
    Model representing an topic of articles
    """
    
    topic = models.CharField(max_length=30, null=True)
    
    def __str__(self):
           """
           String for representing the Model object (in Admin site etc.)
           """
           return self.topic

class Source(models.Model):
    """
    Model representing an news source
    """

    source = models.CharField(max_length=30, help_text='Enter an article source ( e.g. The Times)')

    def __str__(self):
           """
           String for representing the Model object (in Admin site etc.)
           """
           return self.source
           
class Article(models.Model):
    """
    Model representing an article
    """
    # check with the null=True for those other than link
    link = models.OneToOneField('Link', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, null=True)
    topic = models.ForeignKey('Topic', on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField(blank=True, null=True)
    display = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    source = models.ManyToManyField(Source, null=True)
    date_published = models.DateField(null=True, blank=True)
    scientific_rate = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

class Sim_rate(models.Model):
    pair_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for the article pair")
    article1 = models.ForeignKey('Article', on_delete=models.SET_NULL, null=True, related_name='article1')
    article2 = models.ForeignKey('Article', on_delete=models.SET_NULL, null=True, related_name='article2')

    simi_choice = (
        (-3,"totally different"),
        (-2,"almost different"),
        (-1,"a little bit different"),
        (0, "nutral"),
        (1, "a little bit similar"),
        (2, "almost similar"),
        (3, "totally similar")
    )
    similarity = models.FloatField(choices=simi_choice)
    user_id = models.CharField(max_length=30,help_text="User ID",null=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s, %f' % (self.article1, self.article2, self.similarity)
        
    # * thinking about using function to return the name of articles
    

