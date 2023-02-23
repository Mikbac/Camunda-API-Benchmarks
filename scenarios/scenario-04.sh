#!/bin/bash

echo "Starting to remove containers, volume and outputs..."
source ./../tools/clean.sh
echo "Containers and volumes removed"

sleep 1m

echo "Starting containers..."
docker compose -f ./../docker/camunda_7_14_postgres_12_1.yaml up -d &

sleep 5m

echo "Adding indexes..."
docker exec -it camunda-db psql -U camunda -d camunda-engine -c 'CREATE INDEX IF NOT EXISTS act_re_procdef_key ON act_re_procdef (key_)'
docker exec -it camunda-db psql -U camunda -d camunda-engine -c 'CREATE INDEX IF NOT EXISTS act_re_procdef_tenant_id ON act_re_procdef (tenant_id_)'
echo "Indexes added"

echo "Startup installing dependencies..."
pip install -r requirements.txt
echo "Dependencies installed"

echo "Starting to generate data..."
cd ./../generators
python ./benchmark_1_init.py
python ./benchmark_2_init.py
echo "Starting to generate data..."

echo "Starting benchmark..."
cd ./../benchmarks
python ./benchmark_1_start.py > ./../results/output.txt
echo "Benchmark completed"