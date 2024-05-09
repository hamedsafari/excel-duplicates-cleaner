FROM python:3.12.3
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 8080
COPY . .
RUN python manage.py collectstatic
CMD ["uwsgi", "--ini", "uwsgi.ini"]
