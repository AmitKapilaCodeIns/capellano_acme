<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Course guide](#course-guide)
  - [Planning](#planning)
  - [Requirements](#requirements)
  - [User Stories](#user-stories)
    - [View each golf hole guide in ascending order](#view-each-golf-hole-guide-in-ascending-order)
      - [As a golfer I can view each hole description so that I can strategise how to play each hole](#as-a-golfer-i-can-view-each-hole-description-so-that-i-can-strategise-how-to-play-each-hole)
    - [Par and yardage](#par-and-yardage)
      - [As a golfer I can see the par and yardage so that I can plan my shots effectively](#as-a-golfer-i-can-see-the-par-and-yardage-so-that-i-can-plan-my-shots-effectively)
    - [View map](#view-map)
      - [As a golfer I can a visual map or diagram of each hole so that I can understand the terrain and layout](#as-a-golfer-i-can-a-visual-map-or-diagram-of-each-hole-so-that-i-can-understand-the-terrain-and-layout)
    - [Strategy tips](#strategy-tips)
      - [As a golfer I can read strategy tips so that I can avoid common mistakes](#as-a-golfer-i-can-read-strategy-tips-so-that-i-can-avoid-common-mistakes)
    - [Account registration](#account-registration)
      - [As a golf course's resident pro I can register an account so that I can provide hole guides](#as-a-golf-courses-resident-pro-i-can-register-an-account-so-that-i-can-provide-hole-guides)
    - [Approve guides](#approve-guides)
      - [As a Site Admin I can approve or disapprove hole descriptions so that I can filter out descriptions that do not meet criteria](#as-a-site-admin-i-can-approve-or-disapprove-hole-descriptions-so-that-i-can-filter-out-descriptions-that-do-not-meet-criteria)
    - [Manage hole guides](#manage-hole-guides)
      - [As a Site Admin I can create, read, update and delete hole guides so that I can manage my guide content](#as-a-site-admin-i-can-create-read-update-and-delete-hole-guides-so-that-i-can-manage-my-guide-content)
    - [Create drafts](#create-drafts)
      - [As a Site Admin I can create draft guides so that I can finish writing the content later](#as-a-site-admin-i-can-create-draft-guides-so-that-i-can-finish-writing-the-content-later)
    - [View a course](#view-a-course)
      - [As a Site User, I can click on a course so that I can read the full text](#as-a-site-user-i-can-click-on-a-course-so-that-i-can-read-the-full-text)
    - [Read about the site](#read-about-the-site)
      - [As a Site user I can click on the About link so that I can read about the site.](#as-a-site-user-i-can-click-on-the-about-link-so-that-i-can-read-about-the-site)
    - [Add and update the about text](#add-and-update-the-about-text)
      - [As a Site Admin I can create or update the about page content so that it is available on the site](#as-a-site-admin-i-can-create-or-update-the-about-page-content-so-that-it-is-available-on-the-site)
    - [Modify or delete hole guides for a course](#modify-or-delete-hole-guides-for-a-course)
      - [As a Golf Pro I can modify or delete my comments on a hole guide so that I can provide professional tips to players](#as-a-golf-pro-i-can-modify-or-delete-my-comments-on-a-hole-guide-so-that-i-can-provide-professional-tips-to-players)
  - [Features](#features)
  - [Models](#models)
    - [Hole guide model](#hole-guide-model)
    - [Course model](#course-model)
    - [About model](#about-model)
  - [Code](#code)
      - [Files](#files)
      - [Environment variables (env.py)](#environment-variables-envpy)
      - [Database Configuration (settings.py & dj_database_url)](#database-configuration-settingspy--dj_database_url)
      - [Slug Usage](#slug-usage)
      - [Loose Coupling with urls.py](#loose-coupling-with-urlspy)
      - [Static and Media Files](#static-and-media-files)
      - [Templates and views](#templates-and-views)
      - [Code format](#code-format)
      - [Code understandability](#code-understandability)
      - [Code validation](#code-validation)
  - [Testing](#testing)
      - [Manual Testing](#manual-testing)
      - [Error I see when entering a hole number that already exists. This prevents duplicate hole numbers:](#error-i-see-when-entering-a-hole-number-that-already-exists-this-prevents-duplicate-hole-numbers)
      - [Differences Between Manual and Automated Testing](#differences-between-manual-and-automated-testing)
      - [Console](#console)
      - [Accessibility](#accessibility)
      - [HTML](#html)
      - [CSS](#css)
  - [Bugs](#bugs)
    - [The navbar was not visible as I scrolled the HTML page:](#the-navbar-was-not-visible-as-i-scrolled-the-html-page)
    - [Value error HttpResponse object returning none:](#value-error-httpresponse-object-returning-none)
    - [There was no space between hole guides in the HTML page:](#there-was-no-space-between-hole-guides-in-the-html-page)
    - [I encountered this error:](#i-encountered-this-error)
    - [Unfixed Bugs](#unfixed-bugs)
  - [Deployment](#deployment)
    - [Setup Instructions](#setup-instructions)
      - [Install Django](#install-django)
      - [Collect static files](#collect-static-files)
      - [Run Development Server](#run-development-server)
      - [Access the site](#access-the-site)
    - [Version Control](#version-control)
  - [Wireframes](#wireframes)
    - [Home page](#home-page)
    - [Course detail](#course-detail)
    - [About page](#about-page)
    - [Signin page](#signin-page)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Course guide

This project demonstrates the use of **Django Template Language (DTL)** to build a reusable base layout with Bootstrap for styling. The base template provides a consistent navigation bar, footer, and message display system across all pages.

## Planning

-   The site owner's goal is to create an ergonomically presented site that allows amateur golfers to plan their course strategy prior to playing. Golf pros are invited to impart their knowledge of the nuances of each hole on golf courses they have played and know well.

## Requirements

-   The site owner wants readers to enjoy using the site. With that in mind the pages should be visually appealing at the same time simple to use.

-   The site should be responsive, adapting to all screen sizes.

-   Golf pros should be allowed to change their own hole guides in line with how the golf course changes over time.

![Site images in all screens size responsive](./documentation/all-devices-black.png)

---

## User Stories

### View each golf hole guide in ascending order
#### As a golfer I can view each hole description so that I can strategise how to play each hole

-   Given there are numerous holes on the course, the guide for each is listed.

-   When a user selects a course a list of guides is seen

-   Then the user sees all holes in the order in which it will be played.

### Par and yardage
#### As a golfer I can see the par and yardage so that I can plan my shots effectively

-   The par for each hole is visible.

-   The yardage to the centre per tee colour is available.


### View map
#### As a golfer I can a visual map or diagram of each hole so that I can understand the terrain and layout

-   The user can view key hazards (e.g., bunkers, water, OB)

-   The text is clear against the background map

-   The hole detail page loads successfully with HTTP status 200 and no visible rendering errors.


### Strategy tips
#### As a golfer I can read strategy tips so that I can avoid common mistakes

-   The tips are clear and concise

-   The map supports and aligns with the written guide

-   The tips provide aim points with yardages


### Account registration
#### As a golf course's resident pro I can register an account so that I can provide hole guides

-   Given an email a pro can register an account

-   Then the pro can login

-   When the pro is logged in they can add hole descriptions

### Approve guides
#### As a Site Admin I can approve or disapprove hole descriptions so that I can filter out descriptions that do not meet criteria

-   I can approve a hole description.

-   I can disapprove the description.

### Manage hole guides
#### As a Site Admin I can create, read, update and delete hole guides so that I can manage my guide content

-   Given a logged in golf pro, they can create a hole guide for the course they work at

-   Given a logged in user, they can read hole guides for the course they are about to play

-   Given a logged in golf pro, they can update a hole guide

-   Given a logged in golf pro, they can delete a hole guide

### Create drafts
#### As a Site Admin I can create draft guides so that I can finish writing the content later

-   Given a logged in user, they can save a draft hole guide

-   Then they can finish the content at a later time

### View a course
#### As a Site User, I can click on a course so that I can read the full text

-   When a course title is clicked on a detailed view of the course is seen.

### Read about the site
#### As a Site user I can click on the About link so that I can read about the site.

-   When the About link is clicked, the about text is visible.

### Add and update the about text
#### As a Site Admin I can create or update the about page content so that it is available on the site

-   The About app is visible in the admin panel.

### Modify or delete hole guides for a course
#### As a Golf Pro I can modify or delete my comments on a hole guide so that I can provide professional tips to players

-   Given a logged in pro, they can modify their comment

-   Given a logged in pro, they can delete their comment

---

## Features

The site has 6 different course divs per page. Each div has a visually appealing signature picture of the course. A visitor clicks on the course name to find the hole guides. They can then view each hole in ascending order in a simple, clean course detail page. The minimal look complements how simple it is to find the information you need. There are 3 types of user; superuser, editor then reader. Golf pros will be given editor access. Readers are amateur golfers who will be able to register their logins and view the guides.
Their is an about page that allows users to find out more about the creator.

-   Clear Navigation: Easily navigate through different sections of the website. Links will appear within the navbar depending on authentication status. Register and Login appear for anonymous users. Logout links are for logged in users.
-   Responsive Design: The site adapts gracefully to various screen sizes, ensuring optimal usability whether you're browsing on a desktop, tablet, or mobile device. I used Bootstrap 5 integration for responsive design.
-   I used the Django messages framework to provide interactive feedback triggered by user actions.
-   Template content is injected using Django {% block %}

---

## Models

Hole model, Guide model, User model track pro who wrote it. Guide model link to Hole model so that we know which hole has had a guide added to it. The hole and guide models need to link the user model so we know who wrote what.

### Hole guide model

Key | Name | Type | Extra info |
--- | --- | --- | --- |
FK | course | course Model | cascade on delete |
FK | author | User model | cascade on delete |
--- | hole_number | IntegerField |  |
--- | name | CharField | --- |
--- | Par | PositiveSmallIntegerField |  |
--- | Yardage | PositiveIntegerField |  |
--- | stroke_index | PositiveIntegerField |  |
--- | guide | TextField ||
--- | featured_image | CloudinaryField | |
--- | approved | BooleanField | |
--- | created_on | DateTimeField | |

### Course model

Course_name and slug values should be unique to avoid having courses of the same name confusing your users. In Django, the slug is what you'll use to build a URL for each of your posts.

Key | Name | Type | Extra info |
--- | --- | --- | --- |
--- | Course_name | Char(200) | Unique |
--- | Slug (unique) | SlugField | Unique |
FK | Author | User Model | cascade on delete |
--- | featured_image | CloudinaryField | |
--- | contact_info | CharField | |
--- | Content | TextField |  |
--- | created_on | DateTimeField | auto_now_add
--- | Status | Integer |  |
--- | updated_on | DateTimeField | auto_now
---

### About model

- Stores information about the site author

Key | Name | Type | Extra info |
--- | --- | --- | --- |
--- | title | Char(200) | Unique |
--- | updated_on | DateTimeField | auto_now |
--- | profile_image | CloudinaryField | default='placeholder'|
--- | content | TextField() | 

## Code

#### Files

-   Files are grouped in directories by file type
<pre><code>
capellano-milestone3 % ls  *  
db.sqlite3		manage.py		README.md
env.py			Procfile		requirements.txt

__pycache__:
env.cpython-312.pyc	env.cpython-39.pyc

about:
__init__.py	admin.py	migrations	templates	urls.py
__pycache__	apps.py		models.py	tests.py	views.py

calc:
__init__.py	admin.py	migrations	templates	urls.py
__pycache__	apps.py		models.py	tests.py	views.py

capellano_acme:
__init__.py	asgi.py		urls.py
__pycache__	settings.py	wsgi.py

courseguide:
__init__.py	apps.py		migrations	templates	views.py
__pycache__	fixtures	models.py	tests.py
admin.py	forms.py	signals.py	urls.py

documentation:
all-devices-black.png

hole_images:
hole1Addington.png

static:
css	images	js

staticfiles:
admin		css		js
cloudinary	images		summernote

templates:
account		mfa		socialaccount
base.html	openid		tests
</code></pre>

#### Environment variables (env.py)

- Keep sensitive data out of version control.
- Note: Never commit env.py to GitHub. By adding the env.py file to .gitignore, it will not be tracked by git or pushed to GitHub. This keeps our secret information safe by not having it publicly available. For example the os.environ.setdefault command sets an environment variable in the local operating system. We supply the variable name and value in the parentheses. In our case, this is called DATABASE_URL and the value is the URL we copied from our PostgreSQL from Code Institute email.


```
import os

os.environ.setdefault("SECRET_KEY", "your-secret-key")
os.environ.setdefault("DATABASE_URL", "postgres://user:password@hostname:port/dbname")
os.environ.setdefault("CLOUDINARY_URL", "cloudinary://api_key:api_secret@cloud_name")

```

#### Database Configuration (settings.py & dj_database_url)

```
import dj_database_url
from pathlib import Path
import os

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
```
- Heroku will provide the DATABASE_URL via Config Vars. I need to set the environment variable separately on Heroku because, as mentioned, our env.py file is not pushed to GitHub.
- The dj_database_url import is used to convert the database URL we copied from our PostgreSQL from Code Institute email into a format that Django can use to connect to an external database server.

#### Slug Usage
- Used in models.py for SEO-friendly URLs. The slug uses human-readable words, rather than just random characters, to indicate the content of the webpage
```slug = models.SlugField(unique=True)```
- Automatically included in urls.py patterns:
```path('course/<slug:slug>/', views.course_detail, name='course_detail')```

#### Loose Coupling with urls.py
- Each app has its own urls.py. Having one urls.py file per app keeps our apps more modular and independent. This enables an app from one project to be dropped into another.
- Main project urls.py includes them:```path("", include("courseguide.urls"), name="courseguide-urls"),```

#### Static and Media Files
- Cloudinary Storage for media:
```
INSTALLED_APPS = [
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    ...
]
```

#### Templates and views
- In the index.html the for loop iterates over the course_list object: ```{% for course in course_list %}```

This object is passed into the template by the views.py generic ListView, and contains the contents of the queryset we defined earlier.

```
class Course***List***(generic.ListView):
    queryset = ***Course***.objects.all()  # Only show published courses
    template_name = 'courseguide/index.html'  # Template to render the course list
```

- This if statement checks to see how many times our for loop has run. If the counter is divisible by three, then it inserts another closing div tag and a new div with the class of row. This is so that we have a maximum of three posts per row on the homepage

```
  {% if forloop.counter|divisibleby:3 %}
            </div>
            <div class="row">
                {% endif %}
```

- The index.html has DTL tags. For example in the index.html, there's an anchor tag with the class of course-link", which links back to the course details.

```
<a href="{% url 'course_detail' course.slug %}" class="course-link">
<h2 class="card-title">{{ course.course_name }}</h2>
</a>
```

- The course_guide/urls.py has a path that references the course_detail view with the name of *course_detail*.
```
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
```

- So, when Django encounters a url tag, it looks up the name of the URL and inserts it for us.

- At the top of the base.html we are assigning the 'home' URL to a variable named home_url, which is what the as keyword does. 
```
 {% url 'home' as home_url %}
```

- We have to assign it to the variable home_url because the url itself is a tag, so we can't nest a tag inside another tag, so we had to assign the output of url to a variable.

- Then in our if statement it compares request.path, which is our current URL, with the home_url variable. If they're the same, then it inserts the word active into the class names.
```
   <a class="nav-link {% if request.path == home_url %}active{% endif %}" 
```

- We have used DTL logic to add the active attribute to the link for the page we are currently on. 
```
 <li class="nav-item">
  <a class="nav-link {% if request.path == home_url %}active{% endif %}" aria-current="page" href="{% url 'home' %}">Home</a>
</li>
<li class="nav-item">
      <a class="nav-link {% if request.path == about_url %}active{%endif%}" aria-current="page" 
        href="{% url 'about' %}">About</a>
</li>
  {% if user.is_authenticated %}
  <li class="nav-item">
      <a class="nav-link {% if request.path == logout_url %}active{% endif %}" aria-current="page"
          href="{% url 'account_logout' %}">Logout</a>
  </li>
  {% else %}
  <li class="nav-item">
      <a class="nav-link {% if request.path == signup_url %}active{% endif %}" aria-current="page"
          href="{% url 'account_signup' %}">Register</a>
  </li>
  <li class="nav-item">
      <a class="nav-link {% if request.path == login_url %}active{% endif %}" aria-current="page"
          href="{% url 'account_login' %}">Login</a>
  </li>
```

- However, you can see we also have aria-current="page" so that assistive technologies like screen readers know the current
page. This is currently on all page links. This is fixed by moving the endif so it, too, only appears in the rendered link HTML when we are on that specific page.
```
                     <li class="nav-item">
                        <a class="nav-link {% if request.path == home_url %}active" aria-current="page{% endif %}"
                            href="{% url 'home' %}">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link
                          {% if request.path == about_url %}active" aria-current="page{% endif %}"
                            href="{% url 'about' %}">About</a>
                    </li>
                    {% if user.is_authenticated %}
                    <li class="nav-item">
                        <a class="nav-link {% if request.path == logout_url %}active" aria-current="page{% endif %}"
                            href="{% url 'account_logout' %}">Logout</a>
                    </li>
                    {% else %}
                    <li class="nav-item">
                        <a class="nav-link {% if request.path == signup_url %}active" aria-current="page{% endif %}"
                            href="{% url 'account_signup' %}">Register</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link {% if request.path == login_url %}active" aria-current="page{% endif %}"
                            href="{% url 'account_login' %}">Login</a>
                    </li>
                    {% endif %}
```


#### Code format

-   VS code automatically indents HTML, Javascript and CSS to ease readability.

```

for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let holeId = e.target.getAttribute("hole_id");
    deleteConfirm.href = `delete_hole_guide/${holeId}`;
    deleteModal.show();
  });
}

```
#### Code understandability

-   Copious amounts of comments to explain what the code is doing and why.

```
@login_required
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

```

#### Code validation

-   Python code was run through a Linter to analyze code and flag programming errors, bugs, stylistic errors and suspicious constructs.

![Python code linter](./documentation/codeLinter.png)

-   Javascript was run through JSHint without ES6 checks.

![Javascript code linter](./documentation/JSHint.png)

## Testing

#### Manual Testing

-   In addition to automated testing, this project has also been manually tested to ensure everything works as expected. Here are the steps for manual testing:

Open the site in a web browser. Login as an editor. Select a course I want to add to. Add a hole guide. Logout then login as the approver. Go to the admin page. Approve the new hole guide. Logout then login as the editor of the hole.  Check the hole appears. Check the editor can make changes. Check the editor can delete the hole guide. Test the read only user can view the hole guides.

| Feature          | Action                    | Expected result                           | Tested | Passed | Comments |
| ---------------- | ------------------------- | ----------------------------------------- | ------ | ------ | -------- |
| Home             | Click on the "Home" link  | The user is redirected to the main page   | Yes    | Yes    | \-     
| "Course detail" | Click on a course name | The course detail page opens  | Yes    | Yes    | \-       |
| "Edit" button    | Click on "Edit" button    | Form is populated with guide details | Yes    | Yes    | \-       |
| "Delete" button    | Click on "Delete" button    | Modal pops up to confirm deletion | Yes    | Yes    | \-       |
| Pagination    | Click on "next and previous" buttons    | Only 6 courses per page | Yes    | Yes    | \-       |
| Edit/Delete buttons    | Login as pro    | Buttons only for pro that created the hole guide | Yes    | Yes    | \-       |
| Unique hole numbers per course    | Login as pro    | refer to error below  | Yes    | Yes    | \-       |

#### Error I see when entering a hole number that already exists. This prevents duplicate hole numbers:

```
IntegrityError at /augusta-national/
duplicate key value violates unique constraint "courseguide_holeguide_course_id_hole_number_e508ec85_uniq"
DETAIL:  Key (course_id, hole_number)=(4, 3) already exists.
Request Method:	POST
Request URL:	http://127.0.0.1:8000/augusta-national/
Django Version:	4.2.22
Exception Type:	IntegrityError
Exception Value:	
duplicate key value violates unique constraint "courseguide_holeguide_course_id_hole_number_e508ec85_uniq"
DETAIL:  Key (course_id, hole_number)=(4, 3) already exists.
Exception Location:	/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/django/db/backends/utils.py, line 89, in _execute
Raised during:	courseguide.views.course_detail
Python Executable:	/usr/local/bin/python3
Python Version:	3.9.13
Python Path:	
['/Users/amitkapila/Documents/vscode-projects/capellano-milestone3',
 '/Library/Frameworks/Python.framework/Versions/3.9/lib/python39.zip',
 '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9',
 '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload',
 '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages']
Server time:	Sat, 02 Aug 2025 15:25:58 +0000
```

#### Differences Between Manual and Automated Testing

-   Manual testing involves a person performing the tests step by step. It's useful for exploratory testing, usability testing, and ad-hoc testing, and it allows for human observation to find issues automated tests might miss.

-   Automated testing involves writing scripts to perform the tests automatically. It's useful for regression testing, load testing, and repetitive tasks, and it's more reliable and faster for large codebases or long-term projects.

-   Both types of testing are important and have their own strengths and weaknesses. A good testing strategy usually involves a combination of both.


#### Console

-   Manual testing does not generate internal errors on the page or in the console as a result of user actions.

-   ![Validation](./documentation/console-no-errors.png)

#### Accessibility

-   I used Lighthouse within the Chrome Developer Tools to allow me to test the performance, accessibility, best practices and SEO of the website. I confirmed that the colours and fonts are easy to read and that the site is accessible.
-   **INDEX PAGE**  
    ![Lighthouse Index page screenshot ](./documentation/index-lighthouse.png)

-   The website was tested on Chrome, Mozilla, Edge and Safari browsers with no problems found.
-   Links: Tested and confirmed that each link refer to each page, worked as expected,and redirecting the user between the pages ![Screenshot google extension](./documentation/checkmylinks.png)
![Screenshot google extension](./documentation/checkmylinksII.png)

#### HTML

-   [HTML Validator](https://validator.w3.org/#validate_by_upload) was run on each page of the project. A lot of errors were found but fixed.    ![Screenshot HTML page validator](./documentation/html-validator.png)

-   Now there are several errors specifically "Error: Attribute secure not allowed on element img at this point" & "Trailing slash on void elements". Since these are generated by the template code I could not change it.

```

 {% else %}
    {% cloudinary course.featured_image.url width=395 height=269 crop="fill" gravity="auto" alt="Course" %}

```
-   I added data- to the hole_id attribute as the details page was showing the following issue: ![Screenshot HTML page validator](./documentation/html-details-validator.png)

-    Thereafter the validator reported "Document checking completed. No errors or warnings to show".

#### CSS

-   [Vendor prefixes](https://autoprefixer.github.io/) Used Autoprefixer to parse the CSS and add vendor prefixes.
-   [CSS Validator](https://validator.w3.org/#validate_by_upload) no syntax errors were identified.
    ![Screenshot CSS page validator fixed ](./documentation/css-validator.png)


---

## Bugs

###   The navbar was not visible as I scrolled the HTML page:

I adjusted the code to use fixed-top.

```
<nav class="navbar navbar-expand-lg navbar-light bg-navbar fixed-top">
```

This way it is always visible even if you scroll to the bottom. However it took up vertical space, so I added padding to the top of the page content to avoid it being hidden under the navbar. I used DevTools to work how out how much padding to use based on the height of the nav bar:

```
body {
    background-color: #F9FAFC;
    font-family: 'Barlow', sans-serif;
    padding-top: 76px; /* Adjust depending on your navbar height */
}

```

---

###   Value error HttpResponse object returning none:

ValueError at /manor-house/delete_hole_guide/23/
The view courseguide.views.hole_guide_delete didn't return an HttpResponse object. It returned None instead.

-   I knew that Django views must return an HttpResponse. I could see the view function hole_guide_delete _did_ have the required response code.

```

 if hole_guide.author == request.user:
        hole_guide.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            "Your hole guide has been deleted."
            )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            "You do not have permission to delete this hole guide."
        )
        return HttpResponseRedirect(reverse('course_detail', args=[slug]))

```

-   I then deducted that the error was caused by the return statement being in the same column as the else code. I had to restructure the code. I moved the return so that it was on the same column as the if-else blocks. That way one always ends with a return HttpResponseRedirect(...), regardless of which branch the logic goes down.

---

###   There was no space between hole guides in the HTML page:

I wanted to have more space between li elements in the HTML page.

-   Since I was using Bootstrap I wanted to use similar code. I employed the *mb-4* class to be consistent

```
                     {% for hole in hole_guides %}
                    <li class="mb-4">
                        <h3>Hole {{ hole.hole_number }}{% if hole.name %}: {{ hole.name }}{% endif %}</h3>

```

---


###   I encountered this error:

Exception Type:	RuntimeError
Exception Value:	
You called this URL via POST, but the URL doesn't end in a slash and you have APPEND_SLASH set. Django can't redirect to the slash URL while maintaining POST data. Change your form to point to 127.0.0.1:8000/manor-house/edit/21/ (note the trailing slash), or set APPEND_SLASH=False in your Django settings.

I add a slash to `edit/${holeId}/:

```
    // Update form fields with the retrieved content
    submitButton.innerText = "Update";
    holeForm.setAttribute("action", `edit/${holeId}/`);
  });

```


---

### Unfixed Bugs

All bugs identified were fixed

## Deployment

### Setup Instructions

#### Install Django

```
pip3 install django
```

#### Collect static files

```
python3 manage.py collectstatic

```

#### Run Development Server

```
python3 manage.py runserver

```

#### Access the site

-   Open http://127.0.0.1:8000 in your browser.

### Version Control

-   The site was created using VS Code as IDE and pushed to Github to the remote repository 'capellano_acme'.
-   Git commands were employed extensively during development to push the code to the remote repository. Prior to pushing the code to the repo I had to make sure to set Debug=False in the project's settings.py before deploying it to the server else someone can hack the development server and garner sensitive information from the logs. The sequence of Git commands utilized includes:
    -   **git add .**: This command adds the files to the staging area, preparing them for commitment.
    -   **git commit -m "commit message"**: It commits the changes to the local repository queue, marking them as ready for the final step.
    -   **git push**: This command is executed to push all committed code to the remote repository on Github.
    ### Deployment to Github pages
    The site was deployed to GitHub pages. The steps taken to deploy are as follows:
    1. Log in to [Github](https://github.com/);
    2. Navigate to [AmitKapilaCodeIns/capellano_acme](https://github.com/AmitKapilaCodeIns/capellano_acme) in the list of repositories;
    3. In the GitHub repository, navigate to the Settings tab;
    4. In Settings scroll down to GitHub pages which opens in a new page;
    5. From the source section drop-down menu, select the Master Branch;
    6. Once the master branch has been selected, the page is automatically refreshed and a display indicates the successful deployment and the link to the address.
    
    The live link can be accessed here: [Rocket Guides](https://courseguide-c34cc0b394d2.herokuapp.com)
    1. Open your project's Heroku dashboard and click the deploy tab and Deploy Branch.
    2. Open the app.

    ### Cloning Repository Code locally
    -   To clone the repository code locally, follow these steps:
    1. Navigate to the Github repository you wish to clone;
    2. Click on the "Code" button located above all the project files;
    3. Select "HTTPS" and copy the repository link;
    4. Open the IDE of your choice and paste the copied git URL into the IDE terminal;
    5. Press Enter to execute the command;
    6. The project will now be created as a local clone in your IDE.

---

## Wireframes

-   These wireframes were created using simple ASCII-style text during the Scope Plane part of the design and planning process for this project. The site was developed with the Desktop layout method first. The wireframes were therefore drawn with that thought in mind and adapted alongside project changes. , Second picture: Coaching page, Third picture: Member page, Fourth picture: Thank you page.
### Home page
-   ![Screenshot Home Page wireframe ](./documentation/wframeHome.png)
---
### Course detail
-   ![Screenshot Coourse detail page Wiframe ](./documentation/wframeCourseDetail.png)
---
### About page
-   ![Screenshot About page Wiframe](./documentation/wiframeAbout.png)
---
### Signin page
-   ![Screenshot sign in Wiframe](./documentation/wframeSignIn.png)
---



