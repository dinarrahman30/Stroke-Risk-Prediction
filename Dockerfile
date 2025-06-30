# Gunakan image Python resmi
FROM python:3.10-slim

# Set direktori kerja di dalam container
WORKDIR /app

# Salin file ke container
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port Flask
EXPOSE 5000

# Jalankan app Flask dengan Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
