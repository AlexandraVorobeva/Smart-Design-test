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
2.Getting list of currencies of the world.<br>
3.Getting the difference in the exchange rate (ruble) between two dates.<br>

### APIs endpoints:<br>
| requests | url | url parameters| description  |
| ------- | --- | --- | --- |
| GET | /products/all | --- | list  |
| GET | /products/{product_id} | --- | list of currencies of the world |
| GET | /products | --- | list of currencies of the world |
| POST | /currency/all | --- | list of currencies of the world |





## Installation
### Clone the repo:<br>

$ git clone https://github.com/SparklingAcidity/Smart-Design-test <br>
$ cd Smart-Design-tes<br>

### Build your FastAPI image in Docker:
$ docker build -t myimage . <br>

### Run a container based on your image:
$ docker run --name mycontainer -p 8000:8000 myimage <br>

### Docker run 
$ docker-compose up




### API from the browser:
You can work on the API directly in your browser.<br>
You will see the automatic interactive API documentation (provided by Swagger UI).
http://127.0.0.1:8000/docs <br>
![Screenshot]() <br>
![Screenshot]() <br>
or http://127.0.0.1:8000/redoc
![Screenshot]()
