#!/bin/bash

docker container rm -f camunda-engine camunda-db
docker volume rm db-storage
rm -f ./../results/output.txt