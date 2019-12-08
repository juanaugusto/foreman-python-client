import json
import requests


class ForemanAPIClient:

    def __init__(self, host, user, password):

        self.host = host
        self.user = user
        self.password = password
        self.base_url = 'http://%s/api/v2' % self.host

    def _process_query(self, query):
        query = ' and '.join(['%s=%s' % (key, query[key]) for key in query])
        
        return 'search=%s' % query

    def get_hosts(self, query):
        search = self._process_query(query)

        per_page = 9999

        url = '%s/hosts?%s&per_page=%s' % (self.base_url, search, per_page)

        response = requests.get(url, auth=(self.user, self.password))

        response.raise_for_status()
        
        return response.json()['results']

    def add_host_parameter(self, host_id, parameter_name, parameter_value):

        data = {'parameter': {'name': parameter_name, 
                              'value': parameter_value}}

        url = '%s/hosts/%s/parameters' % (self.base_url, host_id)

        response = requests.post(url, auth=(self.user, self.password), data=json.dumps(data), headers={'Content-Type': 'application/json'})

        response.raise_for_status()

    def get_host_parameters(self, host_id):

        url = '%s/hosts/%s/parameters' % (self.base_url, host_id)

        response = requests.get(url, auth=(self.user, self.password))

        response.raise_for_status()

        return response.json()['results']

    def update_host_parameter(self, host_id, parameter_id, parameter_name, parameter_value):

        data = {'parameter': {'name': parameter_name, 
                              'value': parameter_value}}

        url = '%s/hosts/%s/parameters/%s' % (self.base_url, host_id, parameter_id)

        response = requests.put(url, auth=(self.user, self.password), data=json.dumps(data), headers={'Content-Type': 'application/json'})

        response.raise_for_status()

    def delete_host_parameter(self, host_id, parameter_id, parameter_name, parameter_value):

        data = {'parameter': {}}

        url = '%s/hosts/%s/parameters/%s' % (self.base_url, host_id, parameter_id)

        response = requests.delete(url, auth=(self.user, self.password), data=json.dumps(data), headers={'Content-Type': 'application/json'})

        response.raise_for_status()