import logging
import http.client
from decorest import RestClient, GET, on, header, POST, body


http.client.HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
class DrupalClient(RestClient):
    def __init__(self, *args, **kwargs):
        super(DrupalClient, self).__init__(*args, **kwargs)

    @POST('/api/cache_clear/topic')
    @header('content-type', 'application/json')
    @header('accept', 'application/json')
    @body('ids')
    def purge_cache_module_bulk(self, ids):
        """Purge the drupal cache for module"""

    @GET('/api/cache_clear/guide')
    @header('content-type', 'application/json')
    @header('accept', 'application/json')
    @body('ids')
    def purge_cache_assembly_bulk(self, ids):
        """Purge the drupal cache for module"""
