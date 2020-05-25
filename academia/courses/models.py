from django.db import models
from django.urls import reverse
from PIL import Image
import vimeo

# Create your models here.

v_client = vimeo.VimeoClient(
  token='30eb0a94af53902b7ff23cef49cababe',
  key='0a40da44fe971cbd4f2e0c0da00db782dda83fba',
  secret="YcO9PGX+vXugbg1bU4LAeNm6bHMDd708IgmGCYtU"
         "+zSTabxZ1SjUOcJhIz7RkJXRKNABNMfBIM9WNUDFXMa3H1VW7CkegSteERNNKgnkTC4rv4Nvb4Ktj/+Nv7lmVtaR "
)


class Course(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    thumbnail = models.ImageField(default='default.jpg', upload_to='thumbnail_pics')
    # allowed_memberships = models.ManyToManyField(Membership)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, *kwargs)

        img = Image.open(self.thumbnail.path)

        if img.height > 360 or img.width > 241:
            output_size = (360, 241)
            img.thumbnail(output_size)
            img.save(self.thumbnail.path)

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')


class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    position = models.IntegerField()
    video_url = models.CharField(max_length=200)
    dl_content = models.FileField(blank=True, null=True, upload_to='dlc/{course}/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:lesson-detail',
                       kwargs={
                           'course_slug': self.course.slug,
                           'lesson_slug': self.slug
                       })
