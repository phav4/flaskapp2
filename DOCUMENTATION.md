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
      "name": "John Doe",
      "age": 30
  }
  
