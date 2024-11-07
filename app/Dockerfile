# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in container
WORKDIR /app

# Copy the current working directory contents into the container at /app
COPY . /app

# Install any needed packages specified in the requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Expose port 8000 for the Django app
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
