# ---- Base image ----
FROM python:3.13-slim

# ---- Environment settings ----
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# ---- Set working directory ----
WORKDIR /fastf1

# ---- System dependencies ----
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ---- Install Python dependencies ----
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ---- Copy project files ----
COPY . .

# ---- Expose FastAPI port ----
EXPOSE 8000

# ---- Run the application ----
CMD ["uvicorn", "fastf1.main:app", "--reload"]
