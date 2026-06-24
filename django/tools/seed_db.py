"""
seed_db.py - Script to populate the database with realistic mock data.
Run: uv run python django/tools/seed_db.py
"""
import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.hashers import make_password
from core.models import User, Course, Lesson, Class

# Clear existing data
print("🧹 Clearing existing data...")
Class.objects.all().delete()
Lesson.objects.all().delete()
Course.objects.all().delete()
User.objects.all().delete()

# ============================================
# USERS
# ============================================
print("👤 Creating users...")
users_data = [
    {"names": "David", "last_names": "Leon", "email": "david@test.com", "password": "1234"},
    {"names": "Maria", "last_names": "Garcia", "email": "maria@test.com", "password": "1234"},
    {"names": "Carlos", "last_names": "Rodriguez", "email": "carlos@test.com", "password": "1234"},
    {"names": "Ana", "last_names": "Martinez", "email": "ana@test.com", "password": "1234"},
    {"names": "Pedro", "last_names": "Lopez", "email": "pedro@test.com", "password": "1234"},
]

users = []
for data in users_data:
    user = User.objects.create(
        names=data["names"],
        last_names=data["last_names"],
        email=data["email"],
        password=make_password(data["password"])
    )
    users.append(user)
    print(f"  ✅ {user.names} {user.last_names}")

# ============================================
# COURSES
# ============================================
print("\n📚 Creating courses...")
courses_data = [
    {
        "title": "Python para Principiantes",
        "description": "Aprende Python desde cero. Cubre variables, bucles, funciones y estructuras de datos. Ideal para quienes empiezan en programación.",
        "lessons": [
            {"title": "Introducción a Python", "classes": ["¿Qué es Python?", "Instalación", "Primer script", "El intérprete", "Resumen"]},
            {"title": "Variables y Tipos de Datos", "classes": ["Variables", "Strings", "Números", "Booleanos", "Type casting"]},
            {"title": "Estructuras de Control", "classes": ["If/Else", "For loops", "While loops", "Break/Continue", "Ejercicios"]},
            {"title": "Funciones", "classes": ["Definir funciones", "Parámetros", "Return values", "Args/Kwargs", "Ejercicios prácticos"]},
        ]
    },
    {
        "title": "Django REST Framework",
        "description": "Domina la creación de APIs REST con Django. Serializadores, viewsets, autenticación y despliegue en producción.",
        "lessons": [
            {"title": "Fundamentos de DRF", "classes": ["¿Qué es DRF?", "Instalación", "Serializadores", "Primer API", "Testing"]},
            {"title": "ViewSets y Routers", "classes": ["ModelViewSet", "ReadOnlyViewSet", "Routers", "Custom actions", "Nested routes"]},
            {"title": "Autenticación y Permisos", "classes": ["Token Auth", "JWT", "Custom permissions", "Throttling", "Best practices"]},
        ]
    },
    {
        "title": "JavaScript Moderno (ES6+)",
        "description": "Aprende JavaScript moderno con ES6+. Arrow functions, destructuring, async/await y más.",
        "lessons": [
            {"title": "Sintaxis ES6+", "classes": ["Let/Const", "Arrow functions", "Template literals", "Destructuring", "Spread operator"]},
            {"title": "Asincronía", "classes": ["Callbacks", "Promises", "Async/Await", "Fetch API", "Manejo de errores"]},
            {"title": "DOM y Eventos", "classes": ["Selectores", "Event listeners", "Creación de elementos", "Event delegation", "Proyecto práctico"]},
        ]
    },
    {
        "title": "SQL y Bases de Datos",
        "description": "Domina SQL desde cero. Consultas, joins, indexes y diseño de bases de datos relacionales.",
        "lessons": [
            {"title": "Fundamentos SQL", "classes": ["¿Qué es SQL?", "CRUD operations", "WHERE clause", "ORDER BY", "GROUP BY"]},
            {"title": "Joins y Relaciones", "classes": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "Self joins", "Subqueries"]},
            {"title": "Diseño de BD", "classes": ["Normalización", "Primary/Foreign keys", "Indexes", "Migrations", "Best practices"]},
        ]
    },
    {
        "title": "Git y GitHub",
        "description": "Control de versiones con Git. branching, merging, pull requests y flujos de trabajo profesionales.",
        "lessons": [
            {"title": "Git Básico", "classes": ["Init, add, commit", "Log y diff", "Checkout", "Stashing", "Ejercicios"]},
            {"title": "Branching y Merging", "classes": ["Crear branches", "Merge", "Rebase", "Conflictos", "Git flow"]},
            {"title": "GitHub y Colaboración", "classes": ["Push/Pull", "Pull requests", "Code review", "Issues", "GitHub Actions"]},
        ]
    },
]

courses = []
for data in courses_data:
    course = Course.objects.create(
        title=data["title"],
        description=data["description"]
    )
    courses.append(course)
    print(f"  ✅ {course.title}")

    for i, lesson_data in enumerate(data["lessons"]):
        lesson = Lesson.objects.create(
            course=course,
            title=lesson_data["title"],
            order=i + 1
        )

        for j, class_title in enumerate(lesson_data["classes"]):
            Class.objects.create(
                lesson=lesson,
                title=class_title,
                order=j
            )
    print(f"     → {len(data['lessons'])} lecciones creadas")

# ============================================
# ENROLLMENTS
# ============================================
print("\n🎯 Creating enrollments...")
enrollments = [
    (users[0], [courses[0], courses[1], courses[4]]),  # David: Python, Django, Git
    (users[1], [courses[2], courses[3]]),               # Maria: JavaScript, SQL
    (users[2], [courses[0], courses[3]]),               # Carlos: Python, SQL
    (users[3], [courses[1], courses[2]]),               # Ana: Django, JavaScript
    (users[4], [courses[4]]),                            # Pedro: Git
]

for user, enrolled_courses in enrollments:
    for course in enrolled_courses:
        course.users.add(user)
    print(f"  ✅ {user.names} → {len(enrolled_courses)} cursos")

# ============================================
# SUMMARY
# ============================================
print("\n" + "="*50)
print("📊 SEED COMPLETED!")
print("="*50)
print(f"  👤 Users:      {User.objects.count()}")
print(f"  📚 Courses:    {Course.objects.count()}")
print(f"  📝 Lessons:    {Lesson.objects.count()}")
print(f"  🎯 Classes:    {Class.objects.count()}")
print(f"  🔗 Enrollments: {sum(c.users.count() for c in courses)}")
print("="*50)
print("\n🔑 Test accounts:")
print("   Email: david@test.com   Password: 1234")
print("   Email: maria@test.com   Password: 1234")
print("   Email: carlos@test.com  Password: 1234")
print("   Email: ana@test.com     Password: 1234")
print("   Email: pedro@test.com   Password: 1234")
