# RESTful API Project

## Author

* **Javier Valenzani** - *Project creator*

## Implementation

* **Xavier J. Cruz** - *Project implementation*


## Overview

## Introduction
This project explores the domain of RESTful APIs, a cornerstone in web services. You'll learn about the Representational State Transfer (REST) architecture, which ensures scalable, stateless, and cacheable communication systems, facilitating easy integration of web services.

## Learning Objectives
By the end of this project, you should understand:

1. HTTP/HTTPS Basics
2. API Consumption with Command Line
3. API Consumption with Python
4. API Development with http.server
5. API Development with Flask
6. API Security & Authentication
7. API Standards & Documentation with OpenAPI

## Importance
RESTful APIs play a crucial role in integrating different systems in our interconnected digital age. This project will equip you with critical skills for consuming, developing, securing, and documenting APIs, blending technical intricacies with larger design concepts.

## REST API Conceptual Diagram
```
+-------+           +-------+           +---------+           +---------+
|       |  Request  |       |  Process  |         |  Fetch/   |         |
|       |   ----->  |       |  -------> |         |  Modify   |         |
|       |           |       |           |         |  -------> |         |
|       | <-----    |       | <-------  |         |           |         |
|       |  Response |       |  Return   |         |           |         |
+-------+           +-------+           +---------+           +---------+
  Client            Web Server           API Server           Database
```

## Components
- Client: The requester of the service (e.g., web browser or application)
- Web Server: Handles incoming requests, acts as a middleman
- API Server: Processes requests, determines required data or actions
- Database: Stores data that the API might fetch or modify
