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

from contrail_tempest_plugin.services.contrail.json import base
from six.moves.urllib import parse as urllib


class DiscoveryServiceAssignmentClient(base.BaseContrailClient):
    def list_discovery_service_assignments(self, params=None):
        url = '/discovery-service-assignments'
        if params:
            url += '?%s' % urllib.urlencode(params)
        return self.get(url)

    def create_discovery_service_assignments(self, **kwargs):
        url = '/discovery-service-assignments'
        post_body = json.dumps({'discovery-service-assignment': kwargs})
        resp, body = self.post(url, post_body)
        body = json.loads(body)
        return body

    def show_discovery_service_assignments(self, assignment_id):
        url = '/discovery-service-assignment/%s' % str(assignment_id)
        return self.get(url)

    def delete_discovery_service_assignments(self, assignment_id):
        url = '/discovery-service-assignment/%s' % str(assignment_id)
        return self.delete(url)

    def update_discovery_service_assignments(self, assignment_id, **kwargs):
        url = '/discovery-service-assignment/%s' % str(assignment_id)
        post_body = json.dumps({'discovery-service-assignment': kwargs})
        return self.put(url, post_body)