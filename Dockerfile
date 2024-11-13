# Use a base image with Python
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Run the Python app
CMD ["python", "square_root.py"]
