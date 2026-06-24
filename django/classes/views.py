"""
Class-based views for Classroom management.
Uses Django's built-in generic views for CRUD operations.
"""
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from lessons.models import Lesson
from .models import Classroom
from .serializers import ClassroomSerializer


class ClassroomListView(ListView):
    """
    List all classes for a lesson.
    GET /api/lessons/<lesson_id>/classes/
    """
    model = Classroom
    template_name = "classes/classroom_list.html"
    context_object_name = "classrooms"

    def get_queryset(self):
        self.lesson = get_object_or_404(Lesson, id=self.kwargs['lesson_id'])
        return Classroom.objects.filter(lesson=self.lesson)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson'] = self.lesson
        context['course'] = self.lesson.course
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('Accept') == 'application/json':
            return JsonResponse(ClassroomSerializer(context['classrooms'], many=True).data(), safe=False)
        return super().render_to_response(context, **response_kwargs)


class ClassroomDetailView(DetailView):
    """
    Get classroom details by ID.
    GET /api/classes/<id>/
    """
    model = Classroom
    template_name = "classes/classroom_detail.html"
    context_object_name = "classroom"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson'] = self.object.lesson
        context['course'] = self.object.lesson.course
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('Accept') == 'application/json':
            return JsonResponse(ClassroomSerializer(context['classroom']).data())
        return super().render_to_response(context, **response_kwargs)


class ClassroomCreateView(CreateView):
    """
    Create a new classroom for a lesson.
    POST /api/lessons/<lesson_id>/classes/create/
    """
    model = Classroom
    template_name = "classes/classroom_form.html"
    fields = ["title", "order", "duration"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson'] = get_object_or_404(Lesson, id=self.kwargs['lesson_id'])
        context['course'] = context['lesson'].course
        return context

    def form_valid(self, form):
        self.lesson = get_object_or_404(Lesson, id=self.kwargs['lesson_id'])
        form.instance.lesson = self.lesson
        response = super().form_valid(form)
        if self.request.headers.get('Accept') == 'application/json':
            return JsonResponse(ClassroomSerializer(self.object).data(), status=201)
        return response

    def get_success_url(self):
        return reverse_lazy("classroom_list", kwargs={"lesson_id": self.kwargs['lesson_id']})


class ClassroomUpdateView(UpdateView):
    """
    Update an existing classroom.
    PUT /api/classes/<id>/update/
    """
    model = Classroom
    template_name = "classes/classroom_form.html"
    fields = ["title", "order", "duration"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson'] = self.object.lesson
        context['course'] = self.object.lesson.course
        return context

    def get_success_url(self):
        return reverse_lazy("classroom_list", kwargs={"lesson_id": self.object.lesson.id})

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.headers.get('Accept') == 'application/json':
            return JsonResponse(ClassroomSerializer(self.object).data())
        return response


class ClassroomDeleteView(DeleteView):
    """
    Delete a classroom.
    DELETE /api/classes/<id>/delete/
    """
    model = Classroom
    template_name = "classes/classroom_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("classroom_list", kwargs={"lesson_id": self.object.lesson.id})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.headers.get('Accept') == 'application/json':
            self.object.delete()
            return JsonResponse({"message": "Classroom deleted"}, status=204)
        return super().delete(request, *args, **kwargs)
