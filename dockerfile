# Use the official Python image from the Docker Hub
FROM python

# Set the working directory in the container
WORKDIR /app





# Copy the rest of the application code into the container
COPY . /app/

# Install the dependencies
RUN pip install pillow
RUN pip install Django

# Run database migrations and collect static files (optional)
# RUN python manage.py migrate
# RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 7564

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:7564"]
