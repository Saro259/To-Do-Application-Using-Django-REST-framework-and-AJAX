# To-Do-Application-Using-Django-REST-framework-and-AJAX
  This is a to-do application created using Django REST Framework and AJAX. The application allows users to create, view, update, and delete to-do items.
# Installations
  Clone the Repository
    
    git clone https://github.com/Saro259/To-Do-Application-Using-Django-REST-framework-and-AJAX.git
    
  Navigate the Project Directory

    cd your-repository

  Create a virtual environment and activate it.

    cd venv
    cd Scripts
    cd activate

 Migrate the database.

    python manage.py migrate

 Run the development server.

     python manage.py runserver

# Use 

  To create a new to-do item, click on the "Add" button and enter the item details.

  To view the list of to-do items, go to the homepage.

  To update an existing to-do item, click on the "Edit" button and make the necessary changes.

  To delete a to-do item, click on the "Delete" button.

# API Endpoints

The application provides the following API endpoints:

    /task-list/: List all tasks or create a new task.
  
    /task-(update or delete)/<pk>/: Retrieve, update or delete a task.

# Technology credits

This application was created with the help of the following technologies:

    Django
    Django REST Framework
    AJAX
      
