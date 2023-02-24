#!/usr/bin/env python

import json

import requests
import yaml


def get_config():
	with open('config.yaml', 'r') as f:
		return yaml.safe_load(f).get('benchmarks').get('init-2-1')


def deploy_process(diagram, url, diagram_name):
	files = [
		('data', (diagram_name, open(diagram, 'rb'), 'application/octet-stream'))
	]

	requests.request('POST', url, headers={}, data={}, files=files)


def get_variables_payload():
	process_variables_quantity = get_config().get('process-variables-quantity')
	variables = {}

	for i in range(process_variables_quantity):
		variables['proc_var_start_{}'.format(i + 1)] = {
			'value': i + 1,
		}

	return json.dumps({
		'variables': variables
	})


def start_processes():
	url = get_config().get('process').get('start-process-url')

	headers = {
		'Content-Type': 'application/json'
	}

	requests.request('POST', url, headers=headers, data=get_variables_payload())


def deploy_diagrams():
	benchmark_config = get_config().get('process')

	main_process_diagram = benchmark_config.get('main-process-bpmn-diagram')
	main_process_url = benchmark_config.get('deployment-url')
	main_process_diagram_name = benchmark_config.get('main-process-bpmn-diagram')

	subprocess_diagram = benchmark_config.get('subprocess-bpmn-diagram')
	subprocess_url = benchmark_config.get('deployment-url')
	subprocess_diagram_name = benchmark_config.get('subprocess-bpmn-diagram')

	deploy_process(main_process_diagram, main_process_url, main_process_diagram_name)
	deploy_process(subprocess_diagram, subprocess_url, subprocess_diagram_name)


if __name__ == '__main__':
	config = get_config()
	proces_deploy_quantity = config.get('deployment-quantity')
	proceses_quantity = config.get('processes-per-deployment-quantity')

	for i in range(proces_deploy_quantity):
		deploy_diagrams()
		print('{}/{}'.format(i + 1, proces_deploy_quantity))
		for _ in range(proceses_quantity):
			start_processes()
