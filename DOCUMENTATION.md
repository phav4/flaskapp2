# Flask CRUD API Documentation

This document provides detailed information on how to use the Flask CRUD API for managing persons. The API offers basic CRUD (Create, Read, Update, Delete) operations for maintaining a list of persons.

## Table of Contents

1. [Introduction](#introduction)
2. [API Endpoints](#api-endpoints)
    - [1. Create a Person](#1-create-a-person)
    - [2. Read a Person](#2-read-a-person)
    - [3. Update a Person](#3-update-a-person)
    - [4. Delete a Person](#4-delete-a-person)
3. [Request and Response Formats](#request-and-response-formats)
4. [Usage Examples](#usage-examples)
5. [Known Limitations](#known-limitations)
6. [Setting Up and Running the API Locally](#setting-up-and-running-the-api-locally)

## Introduction

The Flask CRUD API provides a simple way to manage a list of persons. Each person record consists of a name and an optional age. The API exposes the following CRUD operations:

## API Endpoints

### 1. Create a Person

- **Endpoint:** `POST /api/person`
- **Description:** Create a new person record with a name and an optional age.
- **Request Body (JSON):**
  ```json
  {
      "name": "Favour",
      "age": 30
  }
  
- **Response:**
- *Success (HTTP Status Code 201):*
```
{
    "message": "Person created successfully"
}
```
- *Error (HTTP Status Code 400):*
```
{
    "error": "Name is required"
}
```
###  2. Read a Person

- **Endpoint:** `GET /api/person/{name}`
- **Description:** Fetch details of a person by their name.
- **Response:**
- *Success (HTTP Status Code 200):*
```
{
    "name": "Favour",
    "age": 30
}
```
- *Error (HTTP Status Code 404):*
```
{
    "error": "Person not found"
}
```
###  3. Update a Person

- **Endpoint:** `PUT /api/person/{name}`
- **Description:** Update details of an existing person by their name.
- *Request Body (JSON):*
```
{
    "age": 31
}
```
- **Response:**
- *Success (HTTP Status Code 200):*
```
{
    "message": "Person updated successfully"
}
```
- *Error (HTTP Status Code 404):*
```
{
    "error": "Person not found"
}
```
### 4. Delete a Person

- **Endpoint:** DELETE `/api/person/{name}`
- **Description:** Delete a person by their name.
- **Response:**
- *Success (HTTP Status Code 200):*
```
{
    "message": "Person deleted successfully"
}
```
- *Error (HTTP Status Code 404):*
```
{
    "error": "Person not found"
}
```


## Request and Response Formats

- Request data should be sent in JSON format.
- Responses are in JSON format and include either a success message or an error message.


## Usage Examples
*Here are some example API requests and responses:*

 **Create a Person (POST /api/person)**
- **Request:**
```
{
    "name": "Oyeleye",
    "age": 25
}
```
- *Response (Success):*
```
{
    "message": "Person created successfully"
}
```
- *Response (Error - Missing Name):*
```
{
    "error": "Name is required"
}
```

  **Read a Person (GET /api/person/{name})**
- **Request:**
```
GET /api/person/Oyeleye 
```
- **Response (Success):**
```
{
    "name": "Oyeleye",
    "age": 25
}
```
- **Response (Error - Person Not Found):**
```
{
    "error": "Person not found"
}
```


##  Known Limitations

This API uses an in-memory list for data storage and is not suitable for production use.
Error handling is minimal and may require improvement for production use.
Authentication and authorization are not implemented. Security measures should be added before deploying to production.

## Setting Up and Running the API Locally

*To deploy the API to a server, follow these steps:*

1. Set up a server environment (e.g., AWS, Heroku, or a VPS).
2. Deploy your code to the server.
3. Configure the server to host the API.
