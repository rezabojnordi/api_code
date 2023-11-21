# weather Application

This project helps you to see the weather condition of Istanbul city

## Features

- FastAPI framework for high performance
- Docker integration for easy deployment
- (Add other features specific to your application)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Docker
- (Any other prerequisites)

### Requirements for deploying this application

* installing Docker and Docker-compose on your server

```bash

curl -fsSL https://get.docker.com -o install-docker.sh
sudo sh install-docker.sh

curl -SL https://github.com/docker/compose/releases/download/v2.23.1/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```
* you must install Ansible on your deploy or your client

```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible
```

### Installing

A step-by-step series of examples that tell you how to get a development environment running:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repository.git


### Docs
if you want to know how to use Api plsease open below Url on your browser

```
http://{ServerAddress}/docs
```
