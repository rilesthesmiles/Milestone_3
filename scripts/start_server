#!/bin/bash
cd /home/ec2-user/app
docker build -t image .
docker run -p 80:8080 --name pokemon image

