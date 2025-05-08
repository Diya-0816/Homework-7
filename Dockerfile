# Use Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install -r requiremen.txt

# Run the script
CMD ["python", "ma.py"]
