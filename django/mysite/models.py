from django.db import models

class User(models.Model):
    names = models.CharField(max_length=200)
    last_names = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.names} {self.last_names}"


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    users = models.ManyToManyField(User, related_name="courses", blank=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.course.title} — {self.title}"


class Class(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="classes")
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        constraints = [
            models.CheckConstraint(
                check=models.Q(order__lt=5),
                name="max_5_classes_per_lesson",
            )
        ]

    def __str__(self):
        return f"{self.lesson.title} — {self.title}"
