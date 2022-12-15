FROM python:3.8
RUN pip install poetry
WORKDIR /code/
COPY poetry.lock pyproject.toml /code/
RUN poetry config virtualenvs.create false && \
    poetry install
COPY . /code/
RUN poetry install
ENTRYPOINT ["my-script"]
CMD ["--help"]
