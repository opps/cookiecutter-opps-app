cookiecutter-opps-app
=====================

Opps app template for [cookiecutter](https://github.com/audreyr/cookiecutter)


# Installing cookiecutter

```pip install cookiecutter```

# Creating a new Opps app using this template

Go to your development directory.

(optional)  
Sometimes it is usefull to develop just inside the virtual env directory, considering virtualenv wrapper.  

```bash
/$ workon opps-env
(opps-env)/$ cdvirtualenv
~/.virtualenvs/opps-env/$ cd src
~/.virtualenvs/opps-env/src$ cookiecutter https://github.com/opps/cookiecutter-opps-app.git
What is your app repo_name? myapp
...
# just answer all the questions
```

and then

```
~/.virtualenvs/opps-env/src$ ls
opps opps-myapp ...
~/.virtualenvs/opps-env/src$ cd opps-myapp
~/.virtualenvs/opps-env/src/opps-myapp$ git init
creating a git repo.....
~/.virtualenvs/opps-env/src/opps-myapp$ git add remote https://your_app_repo_url
~/.virtualenvs/opps-env/src/opps-myapp$ git commit -a -m "initial app created by cookiecutter"
```

