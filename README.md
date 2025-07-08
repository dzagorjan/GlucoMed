# GlucoMed
Distributed systems project for healthcare - Glucomed

The goal of this project is development of a backend system in healthcare that monitors the level of glucose in patients using data from IoT devices, based on a microservices architecture.
Microservices will be implemented for managing reading data, patient management and device management.
The system will be based on a distributed architecture, using Python and FastAPI for API deveploment, DynamoDB as the database, Docker for containerization, and Nginx as a load balancer to ensure high availability and system reliability. The system will be deployed on AWS EC2 using AWS Free Tier.

## Patients API
http://18.194.137.87:8001/docs#/

![Patients API](api_patients.jpg)


## Devices API
http://18.194.137.87:8002/docs#/

![Devices API](api_devices.jpg)


## Readings API
http://18.194.137.87:8003/docs#/

![Readings API](api_readings.jpg)


## Test example using Thunder client - GET patients
![example](get_patients_thunder_client.jpg)


## Test example using Thunder client - PUT patients
![example](put_patients_thunder_client.jpg)


## EC2 - metrics & cloudwatch
![ec2](ec2_metrics.jpg)

![ec2](ec2_cloudwatch.jpg)


