from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Course

# Create your views here.


class CourseList(generic.ListView):
    queryset = Course.objects.filter(status=1)  # Only show published courses
    template_name = 'courseguide/index.html'  # Template to render the course list


def course_detail(request, slug):
    """
    Display an individual :model:`courseguide.Course`.

    **Context**

    ``course``
        An instance of :model:`courseguide.Course`.

    **Template:**

    :template:`courseguide/course_detail.html`
    """

    queryset = Course.objects.filter(status=1)
    course = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "courseguide/course_detail.html",
        {"course": course},
    )
