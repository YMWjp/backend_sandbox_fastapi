# backend_sandbox_fastapi

This project is a backend application built using FastAPI. It is structured to provide a clean architecture with separate layers for domain models, services, repositories, and API endpoints.

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
