# Task Manager Midterm Project

## Project Setup

### 1. Create MySQL Database
Create a MySQL database named `appdb`:
```sql
CREATE DATABASE appdb;
```

### 2. Set Up Virtual Environment
Navigate to the project directory (taskmanager) and activate the virtual environment:
```sh
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install Django and MySQL Client
If Django and MySQL client are not installed, install them using:
```sh
pip install django mysqlclient
```

### 4. Migrate the Models
Run the following command to apply database migrations:
```sh
python manage.py migrate
```

### 5. Start the Django Project
Run the following command to start the Django server:
```sh
python manage.py runserver
```

### 6. Start the application
Click the link on the terminal to open the application
