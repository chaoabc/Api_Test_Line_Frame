import requests
import unittest
from   utils.config_utils import local_config


class APITest(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts =local_config.hosts
    def tearDown(self) -> None:
        pass

    def selete_user_tag(token_value):
        api_url = local_config.hosts + '/cgi-bin/tags/get'
        get_param_data = {
            'access_token': token_value
        }
        response = requests.get(url=api_url,
                                params = get_param_data)
        return response



if __name__=='__main__':
    unittest.main()