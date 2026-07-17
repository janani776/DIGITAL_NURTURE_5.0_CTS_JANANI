# Microservices Architecture

## Services

| Service | Responsibility | Endpoints | Database |
|---|---|---|---|
| Course Service | Course and Department management | /api/courses | course.db |
| Student Service | Student and Enrollment management | /api/students | student.db |
| Auth Service | Login and JWT | /api/auth | auth.db |
| Notification Service | Email notifications | Internal | notification.db |


## Communication

Synchronous communication:
- Uses HTTP requests.
- Immediate response.
- Tight coupling between services.

Asynchronous communication:
- Uses RabbitMQ/Kafka.
- Services communicate using messages.
- Better scalability.
- Eventual consistency.

Use message queues when:
- Large number of events occur.
- Services should work independently.
- Background processing is required.