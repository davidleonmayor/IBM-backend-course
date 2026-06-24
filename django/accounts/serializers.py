"""
Serializers for User model.
"""
from .models import User


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
        }
