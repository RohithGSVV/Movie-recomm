FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

ENV NAME World

CMD ["python", "app.py"]
