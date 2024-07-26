from django.db import models


class Header(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    title_line = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} - {self.designation}'


class Education(models.Model):
    objects = None
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.degree} at {self.institution}'


class Skill(models.Model):
    objects = None
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Experience(models.Model):
    objects = None
    company = models.CharField(max_length=255)
    exp_description = models.TextField()

    def __str__(self):
        return self.company


class Project(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.email}'
