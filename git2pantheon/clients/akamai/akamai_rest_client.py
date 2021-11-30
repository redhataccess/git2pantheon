import requests, logging, json
from ..client import RestClient
from akamai.edgegrid import EdgeGridAuth

logger = logging.getLogger(__name__)


class AkamaiCachePurgeClient:
    def __init__(self,host, client_token, client_secret, access_token):
        self.session: requests.Session = requests.Session()
        self.session.auth = EdgeGridAuth(client_token=client_token, client_secret=client_secret,
                                         access_token=access_token)
        self.host = host
        self.akamai_rest_client = RestClient(auth_session=self.session, verbose=True,
                                                         base_url=self.host)

    def purge(self, purge_obj, action='delete'):
        logger.info('Adding %s request to the queue for %s' % (action, json.dumps(purge_obj)))
        return self.akamai_rest_client.post('/ccu/v3/delete/url', json.dumps(purge_obj))