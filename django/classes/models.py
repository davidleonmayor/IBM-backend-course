from django.db import models


class Classroom(models.Model):
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.CASCADE, related_name="classes")
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)
    duration = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.lesson.title} — {self.title}"
