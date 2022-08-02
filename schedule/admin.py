from django.contrib import admin

from schedule.models.lesson import Lesson


@admin.register(Lesson)
class LessonModelAdmin(admin.ModelAdmin):
    list_display = ('id', )

