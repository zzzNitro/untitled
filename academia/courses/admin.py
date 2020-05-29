from django.contrib import admin
from .models import Course, Lesson, Resource


class ResourceAdmin(admin.StackedInline):
    model = Resource


@admin.register(Lesson)
class Lesson(admin.ModelAdmin):
    inlines = [ResourceAdmin]

    class Meta:
        model = Lesson


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course)



