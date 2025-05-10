from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(help_text="Skill level as a percentage (e.g., 90)")

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='project_images/', blank=True)

    def __str__(self):
        return self.title
