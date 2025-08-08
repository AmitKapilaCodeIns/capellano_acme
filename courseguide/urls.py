from django.urls import path

# from all import views
from . import views

# provide a list of URL patterns. Navigation to these URLs will be handled by the
# views defined in this module.
# This file is used to define the URL routing for the 'calc' app.
# Each path() function maps a URL to a specific view function.
urlpatterns = [
    path(
        '',
        views.CourseList.as_view(),
        name='home'
    ),  # URL for the course list view
    path(
        '<slug:slug>/',
        views.course_detail,
        name='course_detail'
    ),  # URL for course detail view
    path(
        '<slug:slug>/edit/<int:guide_id>/',
        views.hole_guide_edit,
        name='hole_guide_edit'
    ),  # URL for editing a hole guide
    path(
        '<slug:slug>/delete_hole_guide/<int:guide_id>/',
        views.hole_guide_delete,
        name='hole_guide_delete'
    ),  # URL for deleting a hole guide
]
