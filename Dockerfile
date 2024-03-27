FROM python:3.11.5
WORKDIR /app
COPY app.py . /app/

RUN pip install flask
RUN pip install flask_cors
EXPOSE 6000
CMD ["flask","run","--host=10.80.61.19","--port=6000"]