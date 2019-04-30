#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import oslo_messaging as messaging

import esi_leap.conf
from esi_leap.manager import utils

CONF = esi_leap.conf.CONF


class ManagerRPCAPI(object):
    """Client side of the manager RPC API

    API version history:

    * 1.0 - Initial version.
    """

    def __init__(self):
        self._client = messaging.RPCClient(
            target=utils.get_target(),
            transport=messaging.get_rpc_transport(CONF),
        )

    def get_policy(self, context, policy_uuid):
        cctxt = self._client.prepare()
        return cctxt.call(context, 'get_policy', policy_uuid=policy_uuid)