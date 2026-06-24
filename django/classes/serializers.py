"""
Serializers for Classroom model.
"""
from .models import Classroom


class ClassroomSerializer:
    def __init__(self, instance, many=False):
        self.instance = instance
        self.many = many

    def data(self):
        if self.many:
            return [self._serialize(c) for c in self.instance]
        return self._serialize(self.instance)

    def _serialize(self, classroom):
        return {
            "id": classroom.id,
            "lesson": classroom.lesson.id,
            "lesson_title": classroom.lesson.title,
            "course_id": classroom.lesson.course.id,
            "course_title": classroom.lesson.course.title,
            "title": classroom.title,
            "order": classroom.order,
            "duration": classroom.duration,
        }
