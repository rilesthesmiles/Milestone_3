# Use an official Python runtime as a parent image
FROM python:latest
# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the port that the Django app will run on (adjust as needed)
EXPOSE 8080

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
