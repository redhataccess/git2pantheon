from urllib import parse

import json
import logging
import requests

logger = logging.getLogger(__name__)


class RestClient:
    def __init__(self, auth_session, verbose, base_url):
        self.auth_session: requests.Session = auth_session
        self.verbose = verbose
        self.base_url = base_url
        self.errors = self.init_errors_dict()

    def join_path(self, path):
        return parse.urljoin(self.base_url, path)

    def get(self, endpoint, params=None):
        response = self.auth_session.get(self.join_path(endpoint), params=params)
        self.process_response(endpoint, response)
        return response.json()

    def log_verbose(self, endpoint, response):
        if self.verbose:
            logger.info(
                'status=' + str(response.status_code) + ' for endpoint=' + endpoint +
                ' with content type=' + response.headers['content-type']
            )
            logger.info("response body=" + json.dumps(response.json(), indent=2))

    def post(self, endpoint, body, params=None):
        headers = {"content-type": "application/json"}
        response = self.auth_session.post(self.join_path(endpoint), data=body, headers=headers, params=params)
        self.process_response(endpoint, response)
        return response.json()

    def process_response(self, endpoint, response):
        self.check_error(response, endpoint)
        self.log_verbose(endpoint, response)

    @staticmethod
    def init_errors_dict():
        return {
            404: "Call to {URI} failed with a 404 result\n with details: {details}\n",
            403: "Call to {URI} failed with a 403 result\n with details: {details}\n",
            401: "Call to {URI} failed with a 401 result\n with details: {details}\n",
            400: "Call to {URI} failed with a 400 result\n with details: {details}\n"
        }

    def check_error(self, response, endpoint):
        if not 200 >= response.status_code >= 400:
            return
        message = self.errors.get(response.status_code)
        if message:
            raise Exception(message.format(URI=self.join_path(endpoint), details=response.json()))
