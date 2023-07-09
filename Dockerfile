# Use a base image with Python and the desired version
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code to the container
COPY . .

# Expose the port on which your Flask app runs
EXPOSE 5000

# Set the environment variables (if required)
# ENV FLASK_ENV=production

# Define the command to run when the container starts
CMD ["sh", "./start_main_app.sh"]
