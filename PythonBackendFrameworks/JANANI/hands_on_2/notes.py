"""
HANDS-ON 1
Web Framework Foundations & Django Project Setup

Task 1: Understand the Request-Response Cycle

1. Request-Response Cycle
Browser sends a GET request to /api/courses/
        |
        V
URL Router (urls.py)
        |
        V
View (views.py)
        |
        V
Model (models.py)
        |
        V
Database
        |
        V
HTTP Response returned to Browser

2. Middleware

Middleware sits between the request and the view.
It processes incoming requests before they reach the view
and outgoing responses before they are sent to the client.

Examples:
- SecurityMiddleware: Adds security-related HTTP headers.
- SessionMiddleware: Manages user session data.

3. WSGI vs ASGI

WSGI:
- Handles synchronous requests.
- Used by Django by default.

ASGI:
- Handles asynchronous requests.
- Used for WebSockets, async views, and real-time applications.

4. MVC vs MVT

MVC:
Model
View
Controller

Django MVT:
Model -> Model
View -> Template
Controller -> View

In Django, the View performs the Controller's role,
while the Template represents the View.
"""