FROM python:3.12
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 8080
COPY . .
RUN python manage.py collectstatic && useradd worker
USER worker
CMD ["gunicorn", "core.asgi", "-w", "2", "-b", "0.0.0.0:8080", "-k", "uvicorn.workers.UvicornWorker"]
