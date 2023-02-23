#!/usr/bin/env python

import json

import requests
import yaml


def get_config():
	with open('config.yaml', 'r') as f:
		return yaml.safe_load(f).get('benchmarks').get('benchmark-1')


def get_results(process):
	url = get_config().get('count-url')

	payload = json.dumps({
		'processDefinitionKey': process,
		"active": False,
		"variables": [
			{
				"name": "proc_var_start_1",
				"value": "1",
				"operator": "eq"
			}
		]
	})
	headers = {
		'Content-Type': 'application/json'
	}

	response = requests.request('POST', url, headers=headers, data=payload)

	print('For the {} process, {} instances were found in {} seconds.'.format(process,
	                                                                          json.loads(response.text).get('count'),
	                                                                          response.elapsed.total_seconds()))


if __name__ == '__main__':
	get_results(get_config().get('process'))
