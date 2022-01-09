FROM python:3.8

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 80


CMD ["python", "manage.py runserver"]