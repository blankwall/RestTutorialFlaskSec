# Use the official Python image based on Alpine Linux
FROM python:3.9-alpine 

RUN apk add bash
# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

WORKDIR task_service

# Expose the port on which the app will run
EXPOSE 5000

# Run the Flask app
CMD ["python3","app.py"]