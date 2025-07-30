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

<a href='https://monsterone.com/graphics/logo-templates/'>Logo Templates item created by Greenflash - https://monsterone.com</a> is where I got the template from