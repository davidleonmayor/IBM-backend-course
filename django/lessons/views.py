"""
Class-based views for Lesson management.
Uses Django's built-in generic views for CRUD operations.
"""
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from courses.models import Course
from .models import Lesson
from .serializers import LessonSerializer


class LessonListView(ListView):
    """
    List all lessons for a course.
    GET /api/courses/<course_id>/lessons/
    """
    model = Lesson
    template_name = "lessons/lesson_list.html"
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
    template_name = "lessons/lesson_detail.html"
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
    template_name = "lessons/lesson_form.html"
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
        return reverse_lazy("lessons_list", kwargs={"course_id": self.kwargs['course_id']})


class LessonUpdateView(UpdateView):
    """
    Update an existing lesson.
    PUT /api/lessons/<id>/update/
    """
    model = Lesson
    template_name = "lessons/lesson_form.html"
    fields = ["title", "order"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = self.object.course
        return context

    def get_success_url(self):
        return reverse_lazy("lessons_list", kwargs={"course_id": self.object.course.id})

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
    template_name = "lessons/lesson_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("lessons_list", kwargs={"course_id": self.object.course.id})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.headers.get('Accept') == 'application/json':
            self.object.delete()
            return JsonResponse({"message": "Lesson deleted"}, status=204)
        return super().delete(request, *args, **kwargs)
