# Copyright 2016 AT&T Corp
# All Rights Reserved.
#
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
import json
from oslo_log import log as logging

from contrail_tempest_plugin.services.contrail.json import base
from six.moves.urllib import parse as urllib

LOG = logging.getLogger(__name__)


class RoutingClient(base.BaseContrailClient):
    def list_routing_instances(self, params=None):
        url = '/routing-instances'
        if params:
            url += '?%s' % urllib.urlencode(params)
        LOG.debug("\n\nList those instances!\n\n")
        return self.get(url)

    def create_routing_instances(self, **kwargs):
        url = '/routing-instances'
        post_body = json.dumps({'routing-instance': kwargs})
        LOG.debug("\n\nCreate that instance!\n\n")
        resp, body = self.post(url, post_body)
        body = json.loads(body)
        return body

    def show_routing_instances(self, instance_id):
        url = '/routing-instance/%s' % str(instance_id)
        LOG.debug("\n\nGet that instance!\n\n")
        return self.get(url)

    def delete_routing_instances(self, instance_id):
        url = '/routing-instance/%s' % str(instance_id)
        LOG.debug("\n\nDelete that instance!\n\n")
        return self.delete(url)

    def update_routing_instances(self, instance_id, **kwargs):
        url = '/routing-instance/%s' % str(instance_id)
        post_body = json.dumps({'routing-instance': kwargs})
        LOG.debug("\n\nUpdate that instance!\n\n")
        return self.put(url, post_body)