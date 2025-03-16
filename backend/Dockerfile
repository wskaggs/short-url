FROM python:3.12

# Move into the installation directory
WORKDIR /app/

# Install dependencies
COPY ./pyproject.toml /app/pyproject.toml
RUN pip install --no-cache-dir /app

# Copy the project files into the installation directory
COPY . /app

# Start the FastAPI application
CMD ["uvicorn", "main:app", "--workers", "4", "--host", "${HOST}", "--port", "${PORT}"]
