FROM --platform=linux/amd64 python:3.10-bullseye as base
RUN pip install poetry==1.1.14
COPY poetry.toml poetry.lock pyproject.toml /

FROM base as production
RUN poetry config virtualenvs.create false --local && poetry install
COPY /todo_app /todo_app
EXPOSE 8000
ENTRYPOINT poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"

FROM base as development
RUN poetry install -n
EXPOSE 5000
ENTRYPOINT poetry run flask run --host 0.0.0.0

FROM base as test
RUN poetry install -n
COPY /todo_app /todo_app
ENTRYPOINT ["poetry", "run", "pytest"]
