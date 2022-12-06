FROM python:3.7-buster as base
RUN pip install poetry
COPY poetry.toml poetry.lock pyproject.toml /

FROM base as production
RUN poetry install -n --without dev
COPY /todo_app /todo_app
EXPOSE 8000
ENTRYPOINT poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"

FROM base as development
RUN poetry install -n
EXPOSE 5000
ENTRYPOINT poetry run flask run --host 0.0.0.0
