from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    # Deskripsi singkat untuk kartu berita di halaman Home
    short_description = models.CharField(max_length=255, default="", help_text="Deskripsi ringkas untuk card berita")
    # Deskripsi lengkap untuk halaman detail berita (Read More)
    full_description = models.TextField(default="", help_text="Isi konten lengkap berita")
    author = models.CharField(max_length=100)
    image = models.URLField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=200)
    # Deskripsi singkat untuk kartu event di halaman Home
    short_description = models.CharField(max_length=255, help_text="Deskripsi ringkas untuk tampilan card di Home")
    # Deskripsi lengkap untuk halaman detail event
    full_description = models.TextField(help_text="Deskripsi detail untuk halaman View Details")
    date = models.DateField()
    time = models.TimeField(null=True, blank=True, help_text="Contoh: 08:00:00 atau biarkan kosong")
    image = models.URLField(max_length=500, blank=True, null=True)
    is_open_for_public = models.BooleanField(default=True)
    registration_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
class Media(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True, help_text="Deskripsi singkat media (opsional)")
    image = models.URLField(max_length=500, blank=True, null=True, help_text="Direct Link Google Drive gambar")
    link = models.URLField(max_length=500, help_text="Link tujuan (YouTube/Instagram/Drive)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title