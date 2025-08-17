from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    pdf_file = models.FileField(upload_to='uploads/')
    word_file = models.FileField(upload_to='outputs/', null=True, blank=True)
    pdf_output_file = models.FileField(upload_to='outputs/', null=True, blank=True)
    full_text = models.TextField(blank=True, null=True)
    tables_json = models.JSONField(default=list, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Document {self.id}"
