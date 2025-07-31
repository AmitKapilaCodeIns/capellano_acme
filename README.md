Make sure to set Debug=False in the project's settings.py before deploying it to the server else someone can hack your development server and garner sensitive information from your logs.

The MIDDLEWARE section helps you with security.

Since we are making an application we want a database. We will use PostGres

The urls.py file is for the django admin site, but also the urls for your apps.

In Django we have a project (capellano_acme) but I want to create apps within this project. These apps will handle the
features that I want for my project. We already have the admin feature but we want other things like the login app.

Each app has it's own urls.py that handles the mapping of requests.

We will be using templates since that allows us to have dynamic content, within a fixed layout.

Because Django provides 'django.middleware.csrf.CsrfViewMiddleware', middleware we can use this {% csrf_token %} in our templates

Models
Hole model, Guide model, User model track pro who wrote it. Guide model link to Hole model so that we know which hole has had a guide added to it. The hole and guide models need to link the user model so we know who wrote what.

Hole guide model
Key | Name | Type | Extra info |
--- | --- | --- | --- |
FK | course | course Model | cascade on delete |
FK | author | User model | cascade on delete |
--- | hole_number | IntegerField |  |
--- | name | CharField | --- |
--- | Par | PositiveSmallIntegerField |  |
--- | Yardage | PositiveIntegerField |  |
--- | guide | TextField ||
--- | image | ImageField | |
--- | Approved | BooleanField | --- |
--- | created_on | DateTimeField | auto_now_add

Course intro model
Course_name and slug values should be unique to avoid having courses of the same name confusing your users. In Django, the slug is what you'll use to build a URL for each of your posts.
Key | Name | Type | Extra info |
--- | --- | --- | --- |
--- | Course_name | Char(200) | Unique |
--- | Slug (unique) | SlugField | --- |
FK | Author | User Model | cascade on delete |
--- | Content | TextField |  |
--- | created_on | DateTimeField | auto_now_add
--- | Status | Integer |  |

Part 1 - env.py:
By adding the env.py file to .gitignore, it will not be tracked by git or pushed to GitHub. This keeps our secret information safe by not having it publicly available.
In the env.py file, the DATABASE_URL value was copied from our PostgreSQL from Code Institute email when we created our database instance.
The os.environ.setdefault command sets an environment variable in the local operating system. We supply the variable name and value in the parentheses. In our case, this is called DATABASE_URL and the value is the URL we copied from our PostgreSQL from Code Institute email.

Part 2 - settings.py:
The dj_database_url import is used to convert the database URL we copied from our PostgreSQL from Code Institute email into a format that Django can use to connect to an external database server.
The code uses another method from the os module to check if the env.py file path exists. If it does, then it will be imported. If it does not exist, the env import will not be attempted so that no error will occur. For example, when the app runs on Heroku, there will be no env.py file to load, as described above.
This code uses os.environ.get to get the value stored in the DATABASE_URL environment variable. The value is then parsed using dj_database_url to put it in a format that Django can use.
Part 3 - Heroku:
We need to set the environment variable separately on Heroku because, as we mentioned, our env.py file is not pushed to GitHub. This means that when our app is running on Heroku, it won't be able to import the database URL settings. We'll go into more detail on the reasons behind this below.

Keeping secrets secret

Why do we set the DATABASE_URL variable in the environment rather than in the code? In the Django world, the DATABASE_URL is considered a secret. But why is that? It's because it contains sensitive information about your database, including the username, password, and database name. Keeping it a secret ensures the safety of your database from unwanted access. That's why we don't set it in code or allow our env.py file to be pushed to GitHub. Anyone with these details would have full access to your database. That is why we use an environment variable, which is just stored in memory on Heroku and is never shown to anyone else.


The fields and attributes match as follows:
The title attribute with field type CharField() generates a single-line form input type text. It accepts Python string data type.
The slug attribute with field type SlugField() also generates a single-line form input type text. It accepts Python string data type. A slug is a short label only containing letters, numbers, underscores or hyphens. You would use one as a semantic URL path rather than an integer or database row ID.
The author attribute with field type ForeignKey() generates a select drop-down list prepopulated by User database table entries. In this case, as User instances are strings, then string data type options are accepted. This value will ultimately be used to display the author's name beside the post on the webpage.
The content attribute with field type TextField() generates a multi-line textarea input. It accepts Python string data type.
The status attribute with field type IntegerField() corresponds to the select drop-down list of Draft or Published. The IntegerField field type normally generates a number picker input, but this default has been overridden to display a select drop-down with string options.
There is no Created on date picker input as we added the option auto_now_add=True, so the time used in the database table will be the computer's time when the Save button is pressed to submit the form.
The option choices use the STATUS constant to limit the integer choice to 0 or 1 and has mapped these two integers to "Draft" and "Published". Therefore, the dropdown option values are "Draft" or "Published" rather than 0 or 1. These strings are more human-readable than the integers.
Choices are a sequence of 2-tuples where the first value is stored in the database, and the second is displayed as the option in the select form input.
You can also see that the default option for the database is 0, which is an integer.
The model naming convention is to use the singular because the admin panel pluralises the model Post to the form Posts. If you named the model Posts, the admin panel would have Postss. You can also see the model User is pluralised to Users in the admin panel.

The blog project has multiple custom models, such as Post and Comment. It will also incorporate some of Django's built-in models, such as User, Group and Permission. These models and their attributes define the structure of, and communicate with, the database used for your blog.

Although Django does not provide an app-level urls.py file by default, it is good to separate the urls.py files into separate apps because, as stated, this follows the Django design philosophy of loose coupling. Having one urls.py file per app keeps our apps more modular and independent. It also means that we can more easily change URLs without breaking our project. It's good to keep your apps as self-contained as possible. This enables an app from one project to be dropped into another.

In the index.html the for loop iterates over the course_list object. 

{% for course in course_list %}

This object is passed into the template by the generic ListView, and contains the contents of the queryset that we defined earlier.

class Course***List***(generic.ListView):
    queryset = ***Course***.objects.all()  # Only show published courses
    template_name = 'courseguide/index.html'  # Template to render the course list


This if statement checks to see how many times our for loop has run. If the counter is divisible by three, then it inserts another closing div tag and a new div with the class of row. This is so that we have a maximum of three posts per row on the homepage

In the navigation section of base.html, there's an anchor tag with the class of "navbar-brand", which links back to the homepage. What do you notice is different about ? Where do you think the value for 'home' comes from?

<a class="navbar-brand" href="{% url 'home' %}"><span class="brand">c<span class="red-o">o</span>de<span
                        class="thin">|star</span></span></a>

The href is a DTL tag. Inside the tag, we have url and a reference to 'home'. The url tag returns an absolute path reference which is a URL without the domain name. It does this, in our example, for the URL named 'home'. Where does it get this name from? Take a look at the blog/urls.py file, and you will see that our main view has the name of home. So, when Django encounters a url tag, it looks up the name of the URL and inserts it for us.

urlpatterns = [
    path('', views.CourseList.as_view(), name='home'),  # URL for the course list view
]

At the top of the base.html we are assigning the 'home' URL to a variable named home_url, which is what the as keyword does. One last thing. The curious among you might be wondering why we couldn't just say {% if request.path == {% url 'home' %} %}? Why did we have to assign it to a variable? All excellent questions, which I'm sure you were thinking. The reason is that url itself is a tag, so we can't nest a tag inside another tag, so we had to assign the output of url to a variable.

 {% url 'home' as home_url %}

Then our if statement. It compares request.path, which is our current URL, with the home_url variable. If they're the same, then it inserts the word active into the class names.

   <a class="nav-link {% if request.path == home_url %}active{% endif %}" 

But, let's back up a second - what's this request.path business? Where did that come from? Remember that we said a view takes a web request and returns a web response? We have access to the contents of the request object in our views and templates. In this case, request.path is a string representing the full path to the requested page, not including the domain. Sound familiar? It's the same kind of string that is returned by the url tag. We can use this kind of pattern matching and variables in our own projects to improve the UX.

We are using the course_list object. This was created using a bit more magic from the generic ListView in our views.py file. 

class CourseList(generic.ListView):
    queryset = Course.objects.all()  # Only show published courses
    template_name = 'courseguide/index.html'  # Template to render the course list

Django determines this based on the model name (Course) and the view type (List). In this case, the Course model and the generic ListView type.

As we iterate we assign the results to the course variable. This variable is an object containing one single record from our database. We can then display the values using the object name and the field name separated by a dot, course.author, for example.

The benefits of the url tag

The url tag is useful because it helps with the DRY principle. If the URL scheme for your project changes, then you don't need to change every page that has a static URL, like you would in front-end projects. Use named URLs in your urls.py and template files, and you won't need to worry about URLs breaking.


Disabling COLLECTSTATIC

One advantage of using a hosting provider like Heroku is that it knows how to deploy a Django project. As such, it automatically runs collectstatic for us, which means we don't need to do it ourselves. When the DISABLE_COLLECTSTATIC environment variable is set in Heroku, however, then it will not run collectstatic when deploying our project. This is why your Heroku-hosted admin dashboard has been unstyled up to now. You can even see collectstatic is skipped in the build logs.

By removing DISABLE_COLLECTSATIC, Heroku will manage our static files for us automatically every time it deploys. So, from now on, you will not need to run collectstatic manually unless you choose to keep DEBUG set to False in your development environment or if you are deploying to a different hosting provider.

Which is all wonderful and lovely, but why? Why do we need whitenoise, and why can't Django just serve the static files for us as it does in our development environment?

Quite simply, Django does have the ability to serve these files, but its server is not suitable for a production environment. runserver lacks the scalability and security required for a production deployment. In the development environment it happily serves them for us, so we can test our project, but for production we need gunicorn to serve the project and whitenoise to serve the static files.

Middleware?

The name sounds like it came directly out of Tolkien, but the concept behind it is very simple. Remember how we said a view takes a web request and returns a web response? Well, middleware also sits between the request and the response, a bit like a specialised kind of view.

Middleware can modify a request prior to it hitting the view code and then modify the response after the view has created it.

Web request explained using a veggie burger
If the web request and response are like the two halves of a burger bun, then the view is your delicious burger (or veggie burger for me), and middleware is like the lettuce, tomato and cheese that goes around the burger. The primary focus of the meal is the burger and bun, but the other things make it so much more tasty!

Similarly, the request, response and view are the most important things, but the middleware adds additional functionality. In the case of Whitenoise, it modifies the response to load the static files from the staticfiles directory and serve them when a user visits our site.

Note: Middleware often needs to be loaded in a particular order. The documentation for a piece of middleware will tell you where it needs to be in the MIDDLEWARE list in settings.py.

And finally, .python-version

In the text steps, you created a file named python-version. If Heroku finds this file, it will use it to determine which version of Python to run your project with. Using the same version of Python in development and hosted environments means that your application should behave the same in both.

Heroku periodically updates the list of supported Python versions. You can see the current list in the Heroku documentation. If your project needs to be redeployed later, it would be worth checking that your Python version is still current.

Within the index.html template's for-loop, update the anchor element to point to the post_detail view.
<a href="{% url 'post_detail' post.slug %}" class="post-link">
Note: This uses the name, post_detail from the urlpattern and the slug variable value is accessed with the same dot notation as seen for author, title, excerpt and so on.

<a href='https://monsterone.com/graphics/logo-templates/'>Logo Templates item created by Greenflash - https://monsterone.com</a> is where I got the template from