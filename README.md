# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

Create a Trello account and a new board. On the board create a "ToDo" list and a "Done" list. Add the Trello API key, token, Board ID and both List IDs to `.env`.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running the tests

```bash
$ poetry run pytest
```

## Set up a webserver from an Ansible Control Node
 - Add server address to hosts.ini under [webservers]
 - Run `ansible-playbook playbook.yml -i hosts.ini`

## Run with Docker

To run in your dev environment with hot loading:

```
docker compose up
```

To build and run in production:

```
docker build --target production --tag todo-app-prod .
docker run --env-file ./.env --publish 8000:8000 todo-app-prod
```

To build and test:

```
docker build --target test --tag test .
docker run test todo_app/test/unit_tests
docker run --env-file .env.docker test todo_app/test/integration_tests
```

# Manual deployment

```
docker build --target production --tag dsdanielh/dev-ops-todo:prod2 .
docker push dsdanielh/dev-ops-todo:prod2
 curl -dH -X POST "https://\$dh-dev-ops:<deployment_password>@dh-dev-ops.scm.azurewebsites.net/api/registry/webhook"
```

# Links

Dockerhub deployment [here](https://hub.docker.com/repository/docker/dsdanielh/dev-ops-todo/general).

Azure deployment [here](https://dh-dev-ops.azurewebsites.net/).
