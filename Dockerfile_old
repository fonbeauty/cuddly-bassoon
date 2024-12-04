FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./

# Expose the port your app runs on
EXPOSE 8000

# Run the application
CMD ["python", "main.py"]