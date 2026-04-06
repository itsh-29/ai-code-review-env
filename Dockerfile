# Use Python base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy all files into container
COPY . .

# Install required dependencies
RUN pip install --no-cache-dir fastapi uvicorn

# Expose port (HuggingFace uses 7860)
EXPOSE 7860

# Run FastAPI server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]