# Education Service for Prohub Learning Platform

This **Education Service** is part of the prohub.uz learning platform, built to manage educational content such as specialities, modules, and lessons. It is designed to integrate seamlessly with the **Authentication Service** to manage admin users and provide clients with access to educational resources.  

---

## Features  

### Core Features  
1. **Admin User Management**:  
   - Receives logged user messages from the Authentication Service via RabbitMQ.  
   - Saves admin users in its database and grants access to create, update, delete, and read functionalities for managing educational content.  

2. **Educational Content Management** (Admin Access):  
   - Create, update, delete, and retrieve:  
     - **Specialities**: Core fields of study.  
     - **Modules**: Linked to specialities (via ForeignKey).  
     - **Lessons**: Linked to modules (via ForeignKey).  

3. **Client Access**:  
   - **View Only**:  
     - List all specialities.  
     - Retrieve modules by speciality.  
     - Retrieve lessons by module.  

---

## Technologies Used  

- **Django REST Framework (DRF)**: For building APIs.  
- **PostgreSQL**: A robust, open-source relational database system.  
- **RabbitMQ**: Message broker for inter-service communication.  
- **Environment Variables**: Sensitive configurations are stored in a `.env` file.  

---

## Setup and Installation  

Follow these steps to set up the project locally:  

### 1. Prerequisites  
Ensure you have the following installed:  
- **Python (version 3.12.3)**  
- **PostgreSQL**  
- **RabbitMQ**  
- **Git**  

### 2. Clone the Repository  
Download the project to your local machine:  
```bash  
git clone https://github.com/dilshod1405/prohub.uz-education.git
cd prohub.uz-education
```  

### 3. Create a Virtual Environment  
Set up an isolated environment for the project dependencies:  
1. Create the environment:  
   ```bash  
   python3 -m venv venv  
   ```  
2. Activate the environment:  
   - On Linux/Mac: `source venv/bin/activate`  
   - On Windows: `venv\Scripts\activate`  

### 4. Install Dependencies  
Install the required Python libraries:  
```bash  
pip install -r requirements.txt  
```  

### 5. Configure Environment Variables  
Set up a `.env` file in the project root with the following variables:  
```env  
SECRET_KEY=your_secret_key  
DEBUG=True  
DATABASE_NAME=your_database_name  
DATABASE_USER=your_database_user  
DATABASE_PASSWORD=your_database_password  
DATABASE_HOST=127.0.0.1  
DATABASE_PORT=5432  
RABBITMQ_URL=amqp://user:password@localhost:5672/  
```  

### 6. Set Up the Database  
1. Open your PostgreSQL client or GUI tool and create a new database.  
2. Apply the migrations to set up database tables:  
   ```bash  
   python3 manage.py migrate  
   ```  

### 7. Start the Server  
Run the development server:  
```bash  
python3 manage.py runserver  
```  
The application will be accessible at `http://127.0.0.1:8000/`.  

---

## How to Use the Service  

### Admin Access  
Admins can use the service to manage educational content:  
- **Specialities**: Create, update, delete, and retrieve.  
- **Modules**: Manage modules linked to specialities.  
- **Lessons**: Manage lessons linked to modules.  

### Client Access  
Clients can only view educational content:  
- **Get Specialities**: Retrieve all specialities.  
- **Get Modules by Speciality**: Retrieve modules linked to a specific speciality.  
- **Get Lessons by Module**: Retrieve lessons linked to a specific module.  

---

## Deployment Instructions  

To deploy the service in a production environment:  
1. Set `DEBUG=False` in the `.env` file.  
2. Use a production-ready web server like Gunicorn or uWSGI to serve the application.  
3. Configure a reverse proxy like Nginx or Apache for handling incoming requests.  
4. Ensure RabbitMQ is running and reachable via the configured `RABBITMQ_URL`.  

---

## Contact  
For any questions or support, feel free to reach out:  
- **Email**: dilshod.normurodov1392@gmail.com 
- **GitHub**: https://github.com/dilshod1405
- **Telegram**: https://t.me/architect_developer

---
