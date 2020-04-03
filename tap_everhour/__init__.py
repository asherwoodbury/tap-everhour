from tap_kit import main_method, BaseClient, TapExecutor
from tap_kit.utils import get_res_data
from datetime import date
from .streams import STREAMS
import pendulum

REQUIRED_CONFIG_KEYS = ["X-Api-Key"]


class EverhourTap(TapExecutor):
    url = 'https://api.everhour.com/team/time/'
    pagination_type = 'next'
    replication_key_format = 'iso8061'
    auth_type = 'basic_key'

    def build_params(self, stream):
        return {
            'from': '2017-01-01',
            'to': str(pendulum.today().date())
        }

    def build_headers(self):
        return {
            "X-Api-Key": self.config["X-Api-Key"]
        }

    def get_res_data(self, res, key):
        return [record for record in res.json()]

def main():
    main_method(
        REQUIRED_CONFIG_KEYS,
        EverhourTap,
        BaseClient,
        STREAMS
    )

if __name__ == '__main__':
    main()