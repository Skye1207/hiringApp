from django.db import models

# Create your models here.


class Response(models.Model):
    responsibilities = models.TextField()
    tech_skills = models.TextField()
    soft_skills = models.TextField()


class CvTemplate(models.Model):
    sample_CV = models.FileField()


class Requirement(models.Model):
    job_spec = models.FileField()

