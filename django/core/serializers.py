"""
Serializers for converting model instances to JSON.
These are lightweight serializers (not Django REST Framework).
"""
from .models import User, Course, Lesson, Class


class UserSerializer:
    def __init__(self, instance, many=False):
        self.instance = instance
        self.many = many

    def data(self):
        if self.many:
            return [self._serialize(u) for u in self.instance]
        return self._serialize(self.instance)

    def _serialize(self, user):
        return {
            "id": user.id,
            "names": user.names,
            "last_names": user.last_names,
            "email": user.email,
            "courses": [c.id for c in user.courses.all()],
        }


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
            "classes": [c.id for c in lesson.classes.all()],
        }


class ClassSerializer:
    def __init__(self, instance, many=False):
        self.instance = instance
        self.many = many

    def data(self):
        if self.many:
            return [self._serialize(c) for c in self.instance]
        return self._serialize(self.instance)

    def _serialize(self, cls):
        return {
            "id": cls.id,
            "lesson": cls.lesson.id,
            "lesson_title": cls.lesson.title,
            "title": cls.title,
            "content": cls.content,
            "order": cls.order,
        }


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
            "lessons": LessonSerializer(course.lessons.all(), many=True).data(),
        }
