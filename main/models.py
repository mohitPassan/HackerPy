from django.db import models
import markdown2
from django.contrib.auth.models import User

# Create your models here.

class Problem(models.Model):
    LEVEL_CHOICES = [
        (1, "Easy"),
        (2, "Medium"),
        (3, "Difficult")
    ]
    name = models.CharField(max_length = 256)
    description = models.TextField()
    level = models.IntegerField(choices = LEVEL_CHOICES)

    def __str__(self):
        return self.name

    @property #When this is used this method will be used as a property, so '()' will not be necessary. Also known as computed property.
    def description_html(self):
        return markdown2.markdown(self.description)

class Contest(models.Model):
    name = models.CharField(max_length = 256)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    description = models.TextField()
    isPrivate = models.BooleanField(default = False)
    problems = models.ManyToManyField('Problem')

    def __str__(self):
        return self.name

class StudentContest(models.Model):
    contest = models.ForeignKey('Contest', on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.user, self.contest)

class Submission(models.Model):
    LANGUAGES = [
        (1, "CPP"),
        (2, "C"),
        (3, "Java"),
        (4, "Python")
    ]
    
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    contest = models.ForeignKey('Contest', on_delete = models.CASCADE)
    problem = models.ForeignKey('Problem', on_delete = models.CASCADE)
    score = models.IntegerField(null = True)
    createdAt = models.DateTimeField(auto_now_add = True)
    source = models.TextField()
    language = models.IntegerField(choices = LANGUAGES)

    def __str__(self):
        return "{} - {} - {}".format(self.user, self.contest, self.problem)



