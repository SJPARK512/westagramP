
from django.db import models

# Create your models here.
class Posting(models.Model):
    user = models.ForeignKey('user.Account', on_delete=models.CASCADE, related_name='nick')
    img_url = models.URLField(null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'postings'
