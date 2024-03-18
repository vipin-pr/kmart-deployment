# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /kmart

# Install dependencies
COPY kmart/requirements.txt /kmart/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY kmart/. /kmart/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "kinomart.wsgi.application"]