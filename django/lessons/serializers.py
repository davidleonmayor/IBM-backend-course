"""
Serializers for Lesson model.
"""
from .models import Lesson


class LessonSerializer:
    def __init__(self, instance, many=False):
        self.instance = instance
        self.many = many

    def data(self):
        if self.many:
            return [self._serialize(l) for l in self.instance]
        return self._serialize(self.instance)

    def _serialize(self, lesson):
        return {
            "id": lesson.id,
            "course": lesson.course.id,
            "course_title": lesson.course.title,
            "title": lesson.title,
            "order": lesson.order,
        }
