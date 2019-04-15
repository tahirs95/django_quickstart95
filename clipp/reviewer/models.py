from django.db import models
from django.urls import reverse

# Create your models here.
class Course(models.Model):
    guid = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    description = models.TextField(default="Provide Description")
    status = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return f"/course/list/{self.guid}/"
        return reverse("reviewer:course_detail", kwargs={"guid":self.guid})
