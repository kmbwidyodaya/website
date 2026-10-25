from django.db import models
from django.utils.safestring import mark_safe

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
    
class NewsImage(models.Model):
    news = models.ForeignKey(News, related_name='additional_images', on_delete=models.CASCADE)
    image_url = models.URLField(
        verbose_name="Image URL",
        help_text="Masukkan link gambar tambahan",
    )

    def __str__(self):
        return f"Gambar Tambahan - {self.news.title}"

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
    image = models.URLField(blank=True, null=True, help_text="Direct Link Google Drive gambar")
    embed_url = models.URLField(blank=True, null=True, help_text=mark_safe(
            "Ketentuan Pemasangan Embed Link:<br>"
            "1. Untuk YouTube, gunakan link embed (contoh: https://www.youtube.com/embed/VIDEO_ID)<br>"
            "2. Untuk Instagram, gunakan link embed (contoh: https://www.instagram.com/p/POST_ID/embed/)<br>"
            "3. Untuk Google Drive, gunakan link embed (contoh: https://drive.google.com/file/d/FILE_ID/preview)"
        )
    )
    author = models.CharField(max_length=100, default="Admin")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title