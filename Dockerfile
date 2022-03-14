FROM python
ENV PYTHONUNBUFFERED 1

WORKDIR .

COPY requirements.txt ./

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . ./

CMD ["python", "manage.py", "runserver"]
