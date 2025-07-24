# An Endpoint Example With FastAPI

Just to show an example of backend code with endpoints, this mini project uses FastAPI for setting up a server on the default localhost port 8000.

## The libraries
* FastAPI
* Pydantic

### FastAPI
FastAPI is the heart of this project.  It's very fast, and with recent updates to Python, it competes with other frameworks like Node.js, Django's RestFramework, and Flask.

### Pydantic
For creating models of data, Pydantic is used for validation and parsing of payloads.

## Basic Deli API

For entering menu items, `POST` a new item at http://localhost:8000/docs/ and then use `GET` and `DELETE` endpoints to alter the **menu_items** dictionary.

NOTE: Wherever the **menu_items** dictionary is referenced, normally there would be a repository call using something like SQLAlchemy.

## Client Side
**simple_client.py** can be executed while server is running or debugging to see a simple `POST` and `GET` request.
