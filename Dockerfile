FROM python:3.11


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt
COPY ./alembic.ini /code/alembic.ini
COPY ./alembic /code/alembic


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /code/app


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# For production
# CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "app.main:app", "-b", "0.0.0.0:8000"]