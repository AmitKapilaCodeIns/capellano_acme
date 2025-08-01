from django.contrib import messages
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Course, HoleGuide
from .forms import HoleGuideForm

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
    hole_guides = course.holes.filter(approved=True).order_by('hole_number')
    hole_count = course.holes.filter(approved=True).count()

    if request.method == "POST":

        hole_form = HoleGuideForm(data=request.POST)
        if hole_form.is_valid():
            guide = hole_form.save(commit=False)
            guide.course = course
            guide.author = request.user
            guide.save()
            messages.add_message(request, messages.SUCCESS, "Your hole guide has been submitted for approval.")

    hole_form = HoleGuideForm()

    return render(
        request,
        "courseguide/course_detail.html",
        {
            "course": course,
            "hole_guides": hole_guides,
            "hole_count": hole_count,
            "hole_form": hole_form,
        },
    )


def hole_guide_edit(request, slug, guide_id):
    """
    Edit an existing hole guide.

    **Context**

    ``course``
        An instance of :model:`courseguide.Course`.

    ``hole_guide``
        An instance of :model:`courseguide.HoleGuide`.

    **Template:**

    :template:`courseguide/hole_guide_edit.html`
    """

    if request.method == "POST":

        queryset = Course.objects.filter(status=1)
        course = get_object_or_404(queryset, slug=slug)
        hole_guide = get_object_or_404(HoleGuide, pk=guide_id)
        hole_form = HoleGuideForm(data=request.POST, instance=hole_guide)

        if hole_form.is_valid() and hole_guide.author == request.user:
            hole_guide = hole_form.save(commit=False)
            hole_guide.course = course
            hole_guide.approved = False  # Reset approval status on edit
            hole_guide.save()
            messages.add_message(request, messages.SUCCESS, "Your hole guide has been updated and is pending approval.")
        else:
            messages.add_message(request, messages.ERROR, "Error updating the hole guide. Please ensure you are the author!")

    return HttpResponseRedirect(reverse('course_detail', args=[slug]))