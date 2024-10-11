FROM python:3.11-slim-bookworm

WORKDIR /app
EXPOSE 8000

COPY ./requirements.txt /chatbot/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /chatbot/requirements.txt

COPY ./chatbot ./chatbot

CMD ["python", "/app/chatbot/main.py"]