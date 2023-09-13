# Flask CRUD API Documentation

This documentation provides information on how to set up, run, and use the Flask CRUD API for managing persons.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the API](#running-the-api)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributors](#contributors)
- [License](#license)

## Prerequisites

Before getting started, make sure you have the following prerequisites installed:

- Python 3.x
- Flask
- virtualenv (optional, but recommended for isolating your project dependencies)

## Installation

1. Clone this repository to your local machine:
 ```
   git clone https://github.com/phav4/flaskapp2
 ```
2. Navigate to the project directory:
    ```bash
   cd flaskapp2
    ```
3. Create a virtual environment (optional but recommended):
    ```bash
   python -m venv env
    ```
4. Activate the virtual environment:

   On Windows:
         
         venv\Scripts\activate

   On macOS and Linux:
        
         source venv/bin/activate

6. Install project dependencies:
    ```bash
   pip install -r requirements.txt


## Running the API
To run the Flask API locally, use the following command:

    python app.py
    
The API will be available at phav4.pythonanywhere.com/


##  API Endpoints
Create a Person: `POST /api/person`
 
  1. Request Body (JSON):
```
{
    "name": "Favour",
    "age": 30
}
```
  2. Read a Person: `GET /api/person/{name}`
      Replace `{name}` with the name of the person you want to fetch.

  3. Update a Person: `PUT /api/person/{name}`
      Replace `{name}` with the name of the person you want to update.
      Request Body (JSON):
```    
{
    "age": 31
}
```
  4. Delete a Person: `DELETE /api/person/{name}`
       Replace {name} with the name of the person you want to delete.


## Testing
  Postman or Python scripts are usefull tools which can be used in testing the API.


## Deployment
  This api was deployed on a free hostin platform, pythonanywhere.com
        1. Set up a server environment.
        2. Deploy your code to the server.
        3. Configure the server to host the API.


##  Contributors
  Oyeleye Favour

##  License
