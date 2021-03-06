# Portolio with django
> A portfolio of my projects with a Django Web Framework

This is the beginning of a long trip that will go through many topics with Django and Python. Currently the topics used are:
* Setup of my django project
* User Management
* Authentication with Github
* Gallery style page with clickable links to projects that I’ve completed

![portfolio-header](https://user-images.githubusercontent.com/17100228/166137887-122e0064-3b0b-4a68-8a86-534c09bbec02.png)

## Modules
* django==3.2
* django-crispy-forms==1.14.0
* django-environ==0.8.1
* python==3.7.13
* social-auth-app-django==5.0.0
  

## Environment variables
Create an .env file and and store it in app/ next to the /settings folder.
It should contain:
```
SECRET_KEY=<your secret key>
SOCIAL_AUTH_GITHUB_KEY=<your github key>
SOCIAL_AUTH_GITHUB_SECRET=your github secret>
DEBUG=<0 for False | 1 for True>
```


## Usage example

```
git clone https://github.com/pycodebe/django-portfolio.git

cd django-portfolio

conda env create --file ./requirements.yml

conda activate venv

python manage.py migrate

python manage.py runserver 0.0.0.0:8000

Navigate to to http://127.0.0.1:8000
```


## Contributing

1. Fork it (<https://github.com/pycodebe/django-portfolio.git>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request