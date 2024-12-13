[![Dynamic DevOps Roadmap](https://devopshive.net/badges/dynamic-devops-roadmap.svg)](https://github.com/DevOpsHiveHQ/dynamic-devops-roadmap) - phase 2
# app-version-container
This project demonstrates a simple Python application that prints the current app version using Semantic Versioning (starting with v0.0.1) and exits. The application is containerized using Docker for easy deployment and portability.
## Features
print the app version. 
Lightweight and containerized for portability. 
Follows semantic versioning standards.
## Requirements
Python 3.9+
Docker
## Installation and Usage
### Run locally 
#### 1. Clone the repo
```
git clone https://github.com/asmaamaged8/app-version-container.git
cd pp-version-container
```
#### 2. Run the app:
```
python app.py
```
### Run in Docker 
#### 1. Build the docker image 
```
docker build -t version-app:v0.0.1 .
```
#### 2. Run the container
```
docker run app-version:v0.0.1    
```
### Verify the output:
```
current app verion is: v0.0.1
```