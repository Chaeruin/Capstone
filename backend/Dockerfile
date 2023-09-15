FROM python:3

WORKDIR /app
ADD ./requirements.txt /app/
RUN apt-get update && apt-get install -y default-mysql-client libmariadb-dev
RUN pip install -r requirements.txt

ADD ./cap /app/cap/
ADD ./gunicorn /app/gunicorn/
ADD ./manage.py /app/
ADD ./main /app/main/

CMD ["gunicorn", "cap.wsgi", "-c", "gunicorn/prod.py"]
