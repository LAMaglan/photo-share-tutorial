# Info

Photo upload app made using Django, based on follow-along
<br>
tutorial [here](https://www.youtube.com/watch?v=mbYx0TGPADE).The original code is [here](https://github.com/tomitokko/photo_share/tree/main/templates)

# Step 0

Make sure django is installed:
<br>
`pip install django`

# Step 1: create django project

Start a new django project:
<br>
`django-admin startproject <name-of-project>`
`cd` into the newly created project

# Step 2: start django app

<br>
`python manage.py startapp <some-name>`
This will create a new folder within the project folder
<br>
To run the app, do
<br>
`python manage.py runserver`
<br>
Copy the URL and paste in browser

# Step 3: create html template

Create folder `templates/` and get source code
for "index.html" file from [here](https://github.com/tomitokko/photo_share/blob/main/templates/index.html)
<br>
modify `settings.py` to "find" index.html
<br>
create a `urls.py` file in the app folder ("photos"), where you define url-paths
<br>
create index "function" in `<app>/views.py` to render the "index.html"
<br>
now, when going to the URL, just add "/index.html" in the <django-project-folder>/urls.py".
<br>
When app is refreshed, you will have the index.html as the landing page

# Step 4: create a database

Start by opening <app-folder>/models.py
<br>
because it involves users uploading files, need to add to settings.py,
<br>
and add a media/ folder to root dir.. and in <django-project-folder>/urls.py
<br>
with this setup, a file a user uploads will get sent to "/media"
<br>
to commit changes from models to the "database", need to do:
<br>
`python manage.py makemigrations`
and
`python manage.py migrate`

# Step 5: set up admin page

For the "developer" of the django app
<br>
`python manage.py createsuperuser`
<br>
Add username (luigiam), e-mail (admin@gmail.com), and password (**\***)
<br>
now, from homepage of app, just add /admin to the end, to get to admin page
<br>
You can see a database "authentication and authorization" (with'fields' groups and users).
<br>
We will create a photos database, by editing <app-folder>/admin.py
<br>
`admin.site.register(Photo)`
<br>
Now, in admin page, you will see a database called Photos
<br>
you can from this admin page add photos to the photo database

# Step 6: enabling user uploading images

Go to "views.py", and add the following to the index(request) function:

```
if request.method == "POST":
        new_photo = Photo(
            file=request.FILES["img"]
        )  # name as defined by form in index.html
        new_photo.save()
```

<br>
Now, after user has uploaded image, it will be viewable from admin page
<br>
(it gets saved to the "media/" folder)
<br>
The link the the URL shows up after changes in the HTML-file:
<br>
```html
<button type="submit" href="/">Submit</button>
    </div>
      </form>
      <div align="center">
        <h3 style="color: black;"><a href="{{ new_url }}">{{ new_url }}</a></h3>
      </div>
    </div>
  </body>
```
<br>
When appending the image file path to the django-url (our localhost) in web-browser,
<br>
it will open the image in the web browser
