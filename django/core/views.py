"""
Class-based views for the Course Platform.
Uses Django's built-in generic views for CRUD operations.
"""
import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse_lazy
from .models import User, Course, Lesson, Class
from .serializers import UserSerializer, CourseSerializer, LessonSerializer, ClassSerializer


# ============================================
# AUTH VIEWS (Using View base class)
# ============================================

class SignupView(View):
    """
    Class-based view for user signup.
    Handles POST requests to create new users.
    """
    def post(self, request):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        names = data.get("names", "").strip()
        last_names = data.get("last_names", "").strip()
        email = data.get("email", "").strip()
        password = data.get("password", "")

        if not all([names, last_names, email, password]):
            return JsonResponse({"error": "All fields are required"}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email already registered"}, status=400)

        user = User.objects.create(
            names=names,
            last_names=last_names,
            email=email,
            password=make_password(password),
        )

        return JsonResponse(UserSerializer(user).data(), status=201)


class LoginView(View):
    """
    Class-based view for user login.
    Handles POST requests to authenticate users.
    """
    def post(self, request):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        email = data.get("email", "").strip()
        password = data.get("password", "")

        if not all([email, password]):
            return JsonResponse({"error": "Email and password are required"}, status=400)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({"error": "Invalid credentials"}, status=401)

        if not check_password(password, user.password):
            return JsonResponse({"error": "Invalid credentials"}, status=401)

        return JsonResponse(UserSerializer(user).data())


# ============================================
# COURSE VIEWS (Using generic views)
# ============================================

class CourseListView(ListView):
    """
    List all courses.
    GET /api/courses/
    """
    model = Course
    template_name = "core/course_list.html"
    context_object_name = "courses"

    def get_queryset(self):
        return Course.objects.all()

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('Accept') == 'application/json':
            return JsonResponse(CourseSerializer(context['courses'], many=True).data(), safe=False)
        return super().render_to_response(context, **response_kwargs)


class CourseDetailView(DetailView):
    """
    Get course details by ID.
    GET /api/courses/<id>/
    """
    model = Course
    template_name = "core/course_detail.html"
    context_object_name = "course"

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('Accept') == 'application/json':
            return JsonResponse(CourseSerializer(context['course']).data())
        return super().render_to_response(context, **response_kwargs)


class CourseCreateView(CreateView):
    """
    Create a new course.
    POST /api/courses/create/
    """
    model = Course
    template_name = "core/course_form.html"
    fields = ["title", "description"]
    success_url = reverse_lazy("course_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.headers.get('Accept') == 'application/json':
            return JsonResponse(CourseSerializer(self.object).data(), status=201)
        return response


class CourseUpdateView(UpdateView):
    """
    Update an existing course.
    PUT /api/courses/<id>/update/
    """
    model = Course
    template_name = "core/course_form.html"
    fields = ["title", "description"]
    success_url = reverse_lazy("core_course_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.headers.get('Accept') == 'application/json':
            return JsonResponse(CourseSerializer(self.object).data())
        return response


class CourseDeleteView(DeleteView):
    """
    Delete a course.
    DELETE /api/courses/<id>/delete/
    """
    model = Course
    template_name = "core/course_confirm_delete.html"
    success_url = reverse_lazy("core_course_list")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.headers.get('Accept') == 'application/json':
            self.object.delete()
            return JsonResponse({"message": "Course deleted"}, status=204)
        return super().delete(request, *args, **kwargs)


# ============================================
# LESSON VIEWS (Using generic views)
# ============================================

class LessonListView(ListView):
    """
    List all lessons for a course.
    GET /api/courses/<course_id>/lessons/
    """
    model = Lesson
    template_name = "core/lesson_list.html"
    context_object_name = "lessons"

    def get_queryset(self):
        self.course = get_object_or_404(Course, id=self.kwargs['course_id'])
        return Lesson.objects.filter(course=self.course)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = self.course
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('Accept') == 'application/json':
            return JsonResponse(LessonSerializer(context['lessons'], many=True).data(), safe=False)
        return super().render_to_response(context, **response_kwargs)


class LessonDetailView(DetailView):
    """
    Get lesson details by ID.
    GET /api/lessons/<id>/
    """
    model = Lesson
    template_name = "core/lesson_detail.html"
    context_object_name = "lesson"

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('Accept') == 'application/json':
            return JsonResponse(LessonSerializer(context['lesson']).data())
        return super().render_to_response(context, **response_kwargs)


class LessonCreateView(CreateView):
    """
    Create a new lesson for a course.
    POST /api/courses/<course_id>/lessons/create/
    """
    model = Lesson
    template_name = "core/lesson_form.html"
    fields = ["title", "order"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = get_object_or_404(Course, id=self.kwargs['course_id'])
        return context

    def form_valid(self, form):
        self.course = get_object_or_404(Course, id=self.kwargs['course_id'])
        form.instance.course = self.course
        response = super().form_valid(form)
        if self.request.headers.get('Accept') == 'application/json':
            return JsonResponse(LessonSerializer(self.object).data(), status=201)
        return response

    def get_success_url(self):
        return reverse_lazy("core_lesson_list", kwargs={"course_id": self.kwargs['course_id']})


class LessonUpdateView(UpdateView):
    """
    Update an existing lesson.
    PUT /api/lessons/<id>/update/
    """
    model = Lesson
    template_name = "core/lesson_form.html"
    fields = ["title", "order"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = self.object.course
        return context

    def get_success_url(self):
        return reverse_lazy("core_lesson_list", kwargs={"course_id": self.object.course.id})

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.headers.get('Accept') == 'application/json':
            return JsonResponse(LessonSerializer(self.object).data())
        return response


class LessonDeleteView(DeleteView):
    """
    Delete a lesson.
    DELETE /api/lessons/<id>/delete/
    """
    model = Lesson
    template_name = "core/lesson_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("core_lesson_list", kwargs={"course_id": self.object.course.id})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.headers.get('Accept') == 'application/json':
            self.object.delete()
            return JsonResponse({"message": "Lesson deleted"}, status=204)
        return super().delete(request, *args, **kwargs)


# ============================================
# CLASS VIEWS (Using generic views)
# ============================================

class ClassListView(ListView):
    """
    List all classes for a lesson.
    GET /api/lessons/<lesson_id>/classes/
    """
    model = Class
    template_name = "core/class_list.html"
    context_object_name = "classes"

    def get_queryset(self):
        self.lesson = get_object_or_404(Lesson, id=self.kwargs['lesson_id'])
        return Class.objects.filter(lesson=self.lesson)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson'] = self.lesson
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('Accept') == 'application/json':
            return JsonResponse(ClassSerializer(context['classes'], many=True).data(), safe=False)
        return super().render_to_response(context, **response_kwargs)


class ClassDetailView(DetailView):
    """
    Get class details by ID.
    GET /api/classes/<id>/
    """
    model = Class
    template_name = "core/class_detail.html"
    context_object_name = "class_obj"

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('Accept') == 'application/json':
            return JsonResponse(ClassSerializer(context['class_obj']).data())
        return super().render_to_response(context, **response_kwargs)


class ClassCreateView(CreateView):
    """
    Create a new class for a lesson.
    POST /api/lessons/<lesson_id>/classes/create/
    """
    model = Class
    template_name = "core/class_form.html"
    fields = ["title", "content", "order"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson'] = get_object_or_404(Lesson, id=self.kwargs['lesson_id'])
        return context

    def form_valid(self, form):
        self.lesson = get_object_or_404(Lesson, id=self.kwargs['lesson_id'])
        form.instance.lesson = self.lesson
        response = super().form_valid(form)
        if self.request.headers.get('Accept') == 'application/json':
            return JsonResponse(ClassSerializer(self.object).data(), status=201)
        return response

    def get_success_url(self):
        return reverse_lazy("core_class_list", kwargs={"lesson_id": self.kwargs['lesson_id']})


class ClassUpdateView(UpdateView):
    """
    Update an existing class.
    PUT /api/classes/<id>/update/
    """
    model = Class
    template_name = "core/class_form.html"
    fields = ["title", "content", "order"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson'] = self.object.lesson
        return context

    def get_success_url(self):
        return reverse_lazy("core_class_list", kwargs={"lesson_id": self.object.lesson.id})

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.headers.get('Accept') == 'application/json':
            return JsonResponse(ClassSerializer(self.object).data())
        return response


class ClassDeleteView(DeleteView):
    """
    Delete a class.
    DELETE /api/classes/<id>/delete/
    """
    model = Class
    template_name = "core/class_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("core_class_list", kwargs={"lesson_id": self.object.lesson.id})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.headers.get('Accept') == 'application/json':
            self.object.delete()
            return JsonResponse({"message": "Class deleted"}, status=204)
        return super().delete(request, *args, **kwargs)


# ============================================
# ENROLLMENT VIEW (Using View base class)
# ============================================

class EnrollView(View):
    """
    Enroll a user in a course.
    POST /api/enroll/
    """
    def post(self, request):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        course_id = data.get("course_id")
        student_email = data.get("student_email")

        if not course_id or not student_email:
            return JsonResponse({"error": "course_id and student_email are required"}, status=400)

        try:
            course = Course.objects.get(id=course_id)
            student = User.objects.get(email=student_email)
        except (Course.DoesNotExist, User.DoesNotExist):
            return JsonResponse({"error": "Course or user not found"}, status=404)

        if student in course.users.all():
            return JsonResponse({"error": "User already enrolled in this course"}, status=400)

        course.users.add(student)

        return JsonResponse({
            "message": "Successfully enrolled in course",
            "course_id": course_id,
            "student_email": student_email,
        })
