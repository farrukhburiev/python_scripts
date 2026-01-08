FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the trigger bot (it will start the spam script when triggered)
CMD ["python", "dota_trigger.py"]
