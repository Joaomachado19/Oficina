FROM python:3.11.5

WORKDIR /Oficina

COPY  . .

RUN pip install django


EXPOSE 8000

CMD [ "python","manage.py", "runserver", "0.0.0.0:8000" ]