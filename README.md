# Smart-Design-test
## FASTAPI CRUD application.
REST API application for exchange rate.<br>

### Stack of technologies:<br>
-Python >= 3.9<br>
-FastApi<br>
-linter: Black<br>

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python.
The key features are: fast to code, based on the open standards for APIs,
very high performance, minimize code duplication.

### Basic functionality:<br>
1.Web REST API<br>
2.Getting list of all products from the database.<br>
3.Getting information about product by id.<br>
4.Creating new products. <br>
5.Sorting product by name, description or any other parameters.

### APIs endpoints:<br>
| requests | url | description  |
| ------- | --- | --- |
| GET | /products/all | list of all products  |
| GET | /products/{product_id} | finds a product in the database by id |
| GET | /products/{product_parameter} | filter by parameter |
| POST | /currency/all | creates a new product |





## Installation
### Clone the repo:<br>

$ git clone https://github.com/SparklingAcidity/Smart-Design-test <br>
$ cd Smart-Design-tes<br>


### Run in Docker
$ docker-compose up




### API from the browser:
You can work on the API directly in your browser.<br>
You will see the automatic interactive API documentation (provided by Swagger UI).
http://127.0.0.1:8000/docs <br>
![Screenshot](https://github.com/SparklingAcidity/Smart-Design-test/blob/in_process/img_for_deadme/1.png) <br>
![Screenshot](https://github.com/SparklingAcidity/Smart-Design-test/blob/in_process/img_for_deadme/2.png) <br>
![Screenshot](https://github.com/SparklingAcidity/Smart-Design-test/blob/in_process/img_for_deadme/3.png) <br>
or http://127.0.0.1:8000/redoc
![Screenshot](https://github.com/SparklingAcidity/Smart-Design-test/blob/in_process/img_for_deadme/4.png)
