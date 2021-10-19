from flask import Blueprint, jsonify
from flask_executor import Executor
from flask_cors import CORS
from git2pantheon.utils import ApiError
from git2pantheon.clients.akamai.akamai_rest_client import AkamaiCachePurgeClient
from git2pantheon.clients.drupal.drupal_rest_client import DrupalClient
import os

executor = Executor()
akamai_purge_client = AkamaiCachePurgeClient(host=os.getenv('AKAMAI_HOST'),
                                             client_token=os.getenv('AKAMAI_CLIENT_TOKEN'),
                                             client_secret=os.getenv('AKAMAI_CLIENT_SECRET'),
                                             access_token=os.getenv('AKAMAI_ACCESS_TOKEN'))
drupal_client = DrupalClient(os.getenv('DRUPAL_HOST'))
api_blueprint = Blueprint('api', __name__, url_prefix='/api/')
CORS(api_blueprint)


@api_blueprint.errorhandler(ApiError)
def error_handler(apiErr):
    error = {'code': apiErr.err_code if (apiErr.err_code is not None) else apiErr.status_code, 'message': apiErr.message,
             'details': apiErr.details if (apiErr.details is not None) else ""}

    response = jsonify({'error': error})
    response.status_code = apiErr.status_code
    return response

from pantheon_uploader import pantheon
