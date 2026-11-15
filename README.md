
# Webhook Processor

A REST API built with Python and FastAPI to receive, process, and retrieve external system alerts and automation triggers.

## Technology Stack

- Python 3.12
- FastAPI
- Pydantic
- Uvicorn
- Docker
- Docker Compose
- AWS EC2
- Ubuntu Linux

## Project Structure

```text
webhook-processor/
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── README.md
```

## Features

- Receive external alerts through POST requests.
- Validate incoming JSON payloads.
- Simulate processing using a 3-second asynchronous delay.
- Store processed alerts in memory.
- Retrieve all processed alerts through a GET endpoint.
- Containerized deployment using Docker and Docker Compose.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /webhook | Receive and process an alert |
| GET | /alerts | Retrieve all processed alerts |

## Run Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd webhook-processor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the application

```bash
python -m uvicorn main:app --reload
```

The API will be available at:

http://localhost:8000

## Run with Docker

Build and start the application:

```bash
docker compose up --build
```

Run in the background:

```bash
docker compose up -d --build
```

Stop the application:

```bash
docker compose down
```

## Testing the API

Open the interactive Swagger documentation:

http://localhost:8000/docs

### POST /webhook

Example request:

```json
{
  "event_id": "evt_98765",
  "source": "server_1",
  "message": "High CPU",
  "timestamp": "2026-11-11T08:00:00Z"
}
```

Expected response:

```json
{
  "status": "processed",
  "event_id": "evt_98765"
}
```

Processing takes approximately 3 seconds.

### GET /alerts

Returns all successfully processed alerts.

## Live Deployment

The application is deployed on AWS EC2 using Docker and Docker Compose.

**Public API URL:**

http://51.20.9.102:8000

**Swagger Documentation:**

http://51.20.9.102:8000/docs

**Live Endpoints:**

- POST http://51.20.9.102:8000/webhook
- GET http://51.20.9.102:8000/alerts

## Storage

The application currently uses in-memory storage.

Processed alerts remain available while the application process is running. Restarting the application clears the stored alerts.

## Deployment Architecture

External System
    ↓
POST /webhook
    ↓
FastAPI
    ↓
AlertService
    ↓
3-Second Processing Delay
    ↓
In-Memory Storage
    ↓
GET /alerts
