from django.db import models

# Create your models here.
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length = 100, blank=True, default= '')
    code = models.TextField()
    lineons = models.BooleanField(default=False)

    language_choices = (
        ("python", "Python"),
        ("java", "java"),
        ("javaScript", "javaScript"),
        ("c", "C"),
        ("c++", "C++"),

    )

    language = models.CharField(max_length= 100, choices = language_choices, default = 'python')
    style = models.CharField(max_length= 100, default = '')

    def __str__(self):
        return self.title