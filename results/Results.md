# Results

## Scenario 1

Processes:

* 100000 processes [Benchmarks_Process_1.bpmn](..%2Fbpmn-diagrams%2FBenchmarks_Process_1.bpmn)

Process variables per process:

* 50 at the beginning
* 5 in the process

|                              | Test 1 | Test 2 | Test 3 | Average |
|------------------------------|--------|--------|--------|---------|
| **Response time in seconds** |        |        |        |         | 
| **Volume size in GB**        |        |        |        |         | 

## Scenario 1

Processes:

* 100000 processes [Benchmarks_Process_1.bpmn](..%2Fbpmn-diagrams%2FBenchmarks_Process_1.bpmn)

With

* `psql -U camunda -d camunda-engine`
* `CREATE INDEX IF NOT EXISTS act_re_procdef_key ON act_re_procdef (key_)`
* `CREATE INDEX IF NOT EXISTS act_re_procdef_tenant_id ON act_re_procdef (tenant_id_)`

|                              | Test 1 | Test 2 | Test 3 | Average |
|------------------------------|--------|--------|--------|---------|
| **response time in seconds** |        |        |        |         | 
| **volume size in GB**        |        |        |        |         | 
                                                         
