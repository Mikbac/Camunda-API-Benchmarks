#!/bin/bash

echo "Starting to remove containers and volume..."
source ./../tools/clean.sh
echo "Containers and volumes removed"

sleep 1m

echo "Starting containers..."
docker compose -f ./../docker/camunda_7_14_postgres_12_1.yaml up -d &

sleep 5m

echo "Startup installing dependencies..."
pip install -r requirements.txt
echo "Dependencies installed"

echo "Starting to generate data..."
cd ./../generators
python ./benchmark_1_init.py
echo "Starting to generate data..."

echo "Starting benchmark..."
cd ./../benchmarks
python ./benchmark_2_start.py > ./../results/output.txt
echo "Benchmark completed"