FROM python:3.10.11-slim-buster

# Create workDir
RUN mkdir code
WORKDIR code
ENV PYTHONPATH = /code

#upgrade pip if you like here
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy Code
COPY . .

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
