# 🧪 FastAPI Sandbox

A simple sandbox environment for experimenting with **FastAPI** and **Clean Architecture**, containerized with Docker.  
This project provides a practical foundation for building scalable and maintainable backend APIs using modern tools.

## 🚀 Features

- FastAPI for building async web APIs
- **Clean Architecture** design pattern for modular, testable code
- MySQL database with Alembic for migrations
- Dockerized environment for development
- Example endpoints with validation and DB interaction

## 🛠 Tech Stack

- FastAPI
- Clean Architecture
- Docker / Docker Compose
- MySQL
- Alembic
- SQLAlchemy

## 📁 Project Structure

```text
.
├── app/
│   ├── api/            # Routers (entry points)
│   │   └── v1/         # Version 1 of the API
│   │       ├── endpoints/ # API endpoints
│   │       └── router.py  # API router configuration
│   ├── core/           # Configuration and settings
│   │   ├── config.py   # Application configuration
│   │   ├── logging.py  # Logging configuration
│   │   ├── rate_limiting.py # Rate limiting logic
│   │   ├── security.py # Security utilities
│   │   └── utils/      # Utility functions
│   ├── db/             # DB session and migrations
│   │   ├── base.py     # Base class for models
│   │   ├── session.py  # Database session management
│   │   └── repositories/ # Database repositories
│   ├── domain/         # Domain models and schemas
│   │   ├── models/     # Domain models
│   │   └── schemas/    # Pydantic schemas
│   ├── repositories/   # DB access logic
│   │   └── user.py     # User repository
│   ├── services/       # Business logic
│   │   └── user.py     # User service
│   └── main.py         # Application entry point
```

## Project Structure

- **app/main.py**: The entry point of the application.
- **app/api/**: Contains the API routes and endpoints.
- **app/domain/**: Contains the domain models and schemas.
- **app/services/**: Contains the business logic and service classes.
- **app/repositories/**: Handles data access and database operations.
- **app/db/**: Database configuration and connection setup.
- **app/core/**: Core functionalities and utilities.

## Features

- User management with functionalities to create, retrieve, and delete users.
- Asynchronous operations for improved performance.
- Modular architecture for easy maintenance and scalability.

## Getting Started

To run the application, you can use Docker to simplify the setup process. Follow these steps:

1. Build the Docker image:

   ```bash
   docker build -t backend_sandbox_fastapi .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 8000:8000 backend_sandbox_fastapi
   ```

3. Access the API documentation at `http://127.0.0.1:8000/api/v1/docs`.

Alternatively, if you prefer to run the application without Docker, ensure you have Python installed and follow these steps:

1. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:

   ```bash
   uvicorn app.main:app --reload
   ```

3. Access the API documentation at `http://127.0.0.1:8000/api/v1/docs`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
