"""
Class-based views for Course management.
Uses Django's built-in generic views for CRUD operations.
"""
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Course
from .serializers import CourseSerializer


class CourseListView(ListView):
    """
    List all courses.
    GET /api/courses/
    """
    model = Course
    template_name = "courses/course_list.html"
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
    template_name = "courses/course_detail.html"
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
    template_name = "courses/course_form.html"
    fields = ["title", "description"]
    success_url = reverse_lazy("courses_list")

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
    template_name = "courses/course_form.html"
    fields = ["title", "description"]
    success_url = reverse_lazy("courses_list")

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
    template_name = "courses/course_confirm_delete.html"
    success_url = reverse_lazy("courses_list")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.headers.get('Accept') == 'application/json':
            self.object.delete()
            return JsonResponse({"message": "Course deleted"}, status=204)
        return super().delete(request, *args, **kwargs)


class EnrollView(ListView):
    """
    Enroll a user in a course.
    POST /api/enroll/
    """
    def post(self, request):
        import json
        from accounts.models import User
        
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
