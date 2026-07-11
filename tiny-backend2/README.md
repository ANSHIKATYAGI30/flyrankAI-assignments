# Tiny Backend

## Tech Stack

- Flask
- PostgreSQL
- Docker

## Run

docker compose up --build

## Architecture

Routes → Service → Repository → Database

Originally the application used MemoryRepository.

Only the repository implementation changed.

The service layer remained unchanged.

Routes remained unchanged.

## Persistence Test

1. POST /messages

2. docker compose down

3. docker compose up

4. GET /messages

The previously inserted rows still existed because PostgreSQL stores its data in a Docker volume.