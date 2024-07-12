from django.db import models

class ProjectStage(models.Model):
    name = models.CharField(max_length=255)
    due_date = models.DateTimeField(null=True)
    status  = models.IntegerField(null=True)

    def __str__(self):
        return self.name
