"""
Serializers for Course model.
"""
from .models import Course


class CourseSerializer:
    def __init__(self, instance, many=False):
        self.instance = instance
        self.many = many

    def data(self):
        if self.many:
            return [self._serialize(c) for c in self.instance]
        return self._serialize(self.instance)

    def _serialize(self, course):
        return {
            "id": course.id,
            "title": course.title,
            "description": course.description,
            "users": [u.id for u in course.users.all()],
        }
