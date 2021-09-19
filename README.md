# Smart-Design-test
## FASTAPI CRUD application.
REST API application.<br>

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
| GET | /products/all/{product_parameter} | filter by parameter |
| GET | /products/all/{parameter}/{parameter2} | filter by two parameters |
| POST | /currency/all | creates a new product |


## Installation
### Clone the repo:<br>

$ git clone https://github.com/SparklingAcidity/Smart-Design-test <br>
$ cd Smart-Design-test<br>

### Create virtualenv:<br>
$ virtualenv venv<br>
$ source venv/bin/activate<br>


### Dependency:
$ pip install -r requirements.txt<br>

### Run your databese on localhost in Docker:

$ docker run -d -p 27017:27017 mongo

### Run the sample server:<br>
$ uvicorn src.main:app --reload <br>

### Run tests:<br>
$ pytest<br>


### API from the browser:
You can work on the API directly in your browser.<br>
You will see the automatic interactive API documentation (provided by Swagger UI).
http://127.0.0.1:8000/docs <br>


### Examples:<br>
$ http://127.0.0.1:8000/products/all    list of all products <br>
$ http://127.0.0.1:8000/products/{product_id}?id=6122270ef9fa04e0488e318b  finds a product in the database by id<br>
$ http://127.0.0.1:8000/products/all/{product_parameter}?parameter=name  sorts all products by name <br>
$ http://127.0.0.1:8000/products/all/{product_parameter}?parameter=name&value=Alexandra filter by name "Alexandra"<br>
$ http://127.0.0.1:8000/products/all/Alexandra/high filter by two parameters: name "Alexandra", and option "high"
$ http://127.0.0.1:8000/products/new   creates a new product<br>

![Screenshot](https://github.com/SparklingAcidity/Smart-Design-test/blob/in_process/img_for_deadme/1.png) <br>
![Screenshot](https://github.com/SparklingAcidity/Smart-Design-test/blob/in_process/img_for_deadme/2.png) <br>
![Screenshot](https://github.com/SparklingAcidity/Smart-Design-test/blob/in_process/img_for_deadme/3.png) <br>
or http://127.0.0.1:8000/redoc
![Screenshot](https://github.com/SparklingAcidity/Smart-Design-test/blob/in_process/img_for_deadme/4.png)
