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

Hole Description model
Key | Name | Type | Extra info |
--- | --- | --- | --- |
FK | hole | hole Model | cascade on delete |
FK | description_author | User model | cascade on delete |
--- | body | TextField | --- |
--- | Par | TextField |  |
--- | Yardage | TextField |  |

<a href='https://monsterone.com/graphics/logo-templates/'>Logo Templates item created by Greenflash - https://monsterone.com</a> is where I got the template from