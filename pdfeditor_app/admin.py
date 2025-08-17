from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pdf_file', 'word_file', 'pdf_output_file', 'uploaded_at')
