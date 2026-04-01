# University Integration Platform: Hub-and-Spoke using Django and REST API

This project serves as a laboratory exercise (IT322: Integrative Programming) to demonstrate the principles of system integration using a **Hub-and-Spoke Architecture** in the Django Framework. It simulates a centralized platform that connects independent university applications via REST APIs.

## 🎯 Learning Objectives

*   Understand how Django can function as a backend integration platform.
*   Implement RESTful APIs for system-to-system communication.
*   Apply core Enterprise Integration Patterns.

## ⚙️ System Concept: University Integration Platform

The system is broken down into four core Django applications (modules):

| Module | Role |
| :--- | :--- |
| **Student App** (`student_app`) | Stores and exposes student profile data (name, course, email, ID). |
| **Library App** (`library_app`) | Stores records on student fines and amounts due. |
| **Payment App** (`payment_app`) | Records tuition and other payments. |
| **Integration Hub** (`integration_hub`) | Acts as the central layer to route requests, consolidate data, and transform data structures. |

## 🏗️ Architecture and Patterns

### Architecture Used: Hub-and-Spoke

*   **Hub:** The `integration_hub` application acts as the central integration layer.
*   **Spokes:** The `student_app`, `library_app`, and `payment_app` are connected only to the hub, not to each other.
*   **Communication:** All data exchange happens through **REST APIs**.

### Integration Patterns Applied

1.  **Request-Response Pattern:** The central hub initiates API requests to pull data from each subsystem.
2.  **Message Routing Pattern:** The hub determines which API call to route to the correct subsystem based on the user request.
3.  **Data Transformation Pattern:** The hub ensures data received from various apps (e.g., student ID format, JSON structures) is standardized.

## 🚀 Getting Started

### Prerequisites

*   Python (3.x)
*   `pip`

### Installation and Setup (Based on Lab Tasks)

1.  **Create the Project Directory:**
    ```bash
    django-admin startproject university_integration
    cd university_integration
    ```

2.  **Install Dependencies:**
    This project requires the Django REST Framework (DRF).
    ```bash
    pip install django djangorestframework
    ```

3.  **Create Applications (Spokes and Hub):**
    ```bash
    python manage.py startapp student_app
    python manage.py startapp library_app
    python manage.py startapp payment_app
    python manage.py startapp integration_hub
    ```

4.  **Configuration:**
    Add `rest_framework` and the new apps to `INSTALLED_APPS` in `settings.py`.

5.  **Define Models:**
    Define the basic models (`Student`, `LibraryRecord`, `Payment`) in their respective `models.py` files (as shown in the lab instructions).

6.  **Run Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7.  **Implement APIs:**
    Create serializers and `ViewSet` classes for the models in each app to expose the REST API endpoints, enabling the hub to communicate with them.