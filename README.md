## Aluxion Test

This application is meant to serve as knowledge test in Python, ORM and Docker.
Given previous conversations, I have decided to use Django (DRF) and its ORM to solve the problem.

### Prerequisites

In order to run the application on a local environment, the following software installations are required:
* Docker Desktop 
(tested in Mac OS. Complete Docker installation, including Docker Compose, required for Windows and Linux distros)

### Installation

In order to deploy to docker container, install dependencies, create database structure, and load initial data, 
open a terminal window in the current directory, and execute the following:

```
docker-compose up -d
```
The result of this operation will be a the app deployed to a Docker container, with port 8000 open and serving the 
Django RF application.
### Tests

In order to run the automated django tests, execute the following in a command terminal:

```
docker exec -it aluxiontest-web-1 python3 manage.py test 
```

A Postman collection file is included for further testing (postman_collection.json).

### API Endpoints
    
* **/api/v1/artists** (Artist list)
* **/api/v1/albums** (Album list with associated tracks)
* **/api/v1/artists-albums** (Artist list with associated albums)
* **/api/v1/albums-enriched** (Album list with artist and track count)

All endpoints can be filtered by key, as follows:

* **/api/v1/artists/1**
* **/api/v1/albums/2**
* **/api/v1/artists-albums/1**
* **/api/v1/albums-enriched/9**





