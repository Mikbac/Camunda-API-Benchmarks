# Results

-----------------------------------------------------------------------------------------

## Scenario 1

Historic count with filters after processDefinitionKey and values.

Processes:

* 100000 processes [Benchmarks_Process_1.bpmn](..%2Fbpmn-diagrams%2FBenchmarks_Process_1.bpmn)

Process variables per process:

* 50 at the beginning
* 5 in the process

Generator config:

```yml
# init-1-1
deployment-quantity: 50
processes-per-deployment-quantity: 2000
process-variables-quantity: 50
```

|                              | Test 1    | Test 2    | Test 3    | Average   |
|------------------------------|-----------|-----------|-----------|-----------|
| **Response time in seconds** | 12.685171 | 12.835809 | 16.952727 | 14.157902 | 
| **Volume size in GB**        | 13.83     | 13.84     | 13.84     | 13.836666 | 

-----------------------------------------------------------------------------------------

## Scenario 2

Historic count with filters after processDefinitionKey and values.

Processes:

* 100000 processes [Benchmarks_Process_1.bpmn](..%2Fbpmn-diagrams%2FBenchmarks_Process_1.bpmn)

Process variables per process:

* 50 at the beginning
* 5 in the process

Generator config:

```yml
# init-1-1
deployment-quantity: 50
processes-per-deployment-quantity: 2000
process-variables-quantity: 50
```

With indexes:

* `CREATE INDEX IF NOT EXISTS act_re_procdef_key ON act_re_procdef (key_)`
* `CREATE INDEX IF NOT EXISTS act_re_procdef_tenant_id ON act_re_procdef (tenant_id_)`

|                              | Test 1    | Test 2    | Test 3    | Average   |
|------------------------------|-----------|-----------|-----------|-----------|
| **Response time in seconds** | 23.672654 | 18.013822 | 19.870712 | 20.519062 | 
| **Volume size in GB**        | 13.83     | 13.81     | 13.84     | 13.826666 | 

-----------------------------------------------------------------------------------------

## Scenario 3

Historic count with filters after processDefinitionKey and values.

Processes:

* 25000 processes [Benchmarks_Process_1.bpmn](..%2Fbpmn-diagrams%2FBenchmarks_Process_1.bpmn)
* 15000 processes [Benchmarks_Process_2_1.bpmn](..%2Fbpmn-diagrams%2FBenchmarks_Process_2_1.bpmn)
* 60000 processes [Benchmarks_Process_2_2.bpmn](..%2Fbpmn-diagrams%2FBenchmarks_Process_2_2.bpmn)

Process variables per process:

* Benchmarks_Process_1:
    * 50 at the beginning
    * 5 in the process
* Benchmarks_Process_2_1:
    * 50 at the beginning
    * 2 in the process
* Benchmarks_Process_2_2:
    * 5 in the process

Generator config:

```yml
# init-1-2
# init-2-1
init-1-2:
  deployment-quantity: 25
  processes-per-deployment-quantity: 1000
  process-variables-quantity: 50
init-2-1:
  deployment-quantity: 15
  processes-per-deployment-quantity: 1000
  process-variables-quantity: 50
```

|                              | Test 1 | Test 2 | Test 3 | Average |
|------------------------------|--------|--------|--------|---------|
| **Response time in seconds** |        |        |        |         | 
| **Volume size in GB**        |        |        |        |         | 

-----------------------------------------------------------------------------------------

## Scenario 4

Historic count with filters after processDefinitionKey and values.

Processes:

* 25000 processes [Benchmarks_Process_1.bpmn](..%2Fbpmn-diagrams%2FBenchmarks_Process_1.bpmn)
* 15000 processes [Benchmarks_Process_2_1.bpmn](..%2Fbpmn-diagrams%2FBenchmarks_Process_2_1.bpmn)
* 60000 processes [Benchmarks_Process_2_2.bpmn](..%2Fbpmn-diagrams%2FBenchmarks_Process_2_2.bpmn)

Process variables per process:

* Benchmarks_Process_1:
    * 50 at the beginning
    * 5 in the process
* Benchmarks_Process_2_1:
    * 50 at the beginning
    * 2 in the process
* Benchmarks_Process_2_2:
    * 5 in the process

Generator config:

```yml
# init-1-2
# init-2-1
init-1-2:
  deployment-quantity: 25
  processes-per-deployment-quantity: 1000
  process-variables-quantity: 50
init-2-1:
  deployment-quantity: 15
  processes-per-deployment-quantity: 1000
  process-variables-quantity: 50
```

With indexes:

* `CREATE INDEX IF NOT EXISTS act_re_procdef_key ON act_re_procdef (key_)`
* `CREATE INDEX IF NOT EXISTS act_re_procdef_tenant_id ON act_re_procdef (tenant_id_)`

|                              | Test 1 | Test 2 | Test 3 | Average |
|------------------------------|--------|--------|--------|---------|
| **Response time in seconds** |        |        |        |         | 
| **Volume size in GB**        |        |        |        |         | 

-----------------------------------------------------------------------------------------

## Scenario 5

Historic count with filter after processDefinitionKey.

Processes:

* 100000 processes [Benchmarks_Process_1.bpmn](..%2Fbpmn-diagrams%2FBenchmarks_Process_1.bpmn)

Process variables per process:

* 50 at the beginning
* 5 in the process

Generator config:

```yml
# init-1-1
deployment-quantity: 50
processes-per-deployment-quantity: 2000
process-variables-quantity: 50
```

|                              | Test 1   | Test 2   | Test 3   | Average  |
|------------------------------|----------|----------|----------|----------|
| **Response time in seconds** | 0.344852 | 0.305457 | 0.706009 | 0.452106 | 
| **Volume size in GB**        | 13.84    | 13.84    | 13.84    | 13.84    | 
