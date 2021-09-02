from decorest import RestClient, GET, on, header, POST, body


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
