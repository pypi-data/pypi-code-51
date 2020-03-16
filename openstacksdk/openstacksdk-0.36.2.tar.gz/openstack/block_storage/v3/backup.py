# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from openstack import exceptions
from openstack import resource
from openstack import utils


class Backup(resource.Resource):
    """Volume Backup"""
    resource_key = "backup"
    resources_key = "backups"
    base_path = "/backups"

    # TODO(gtema): Starting from ~3.31(3.45) Cinder seems to support also fuzzy
    # search (name~, status~, volume_id~). But this is not documented
    # officially and seem to require microversion be set
    _query_mapping = resource.QueryParameters(
        'all_tenants', 'limit', 'marker', 'project_id',
        'name', 'status', 'volume_id',
        'sort_key', 'sort_dir')

    # capabilities
    allow_fetch = True
    allow_create = True
    allow_delete = True
    allow_list = True
    allow_get = True

    #: Properties
    #: backup availability zone
    availability_zone = resource.Body("availability_zone")
    #: The container backup in
    container = resource.Body("container")
    #: The date and time when the resource was created.
    created_at = resource.Body("created_at")
    #: data timestamp
    #: The time when the data on the volume was first saved.
    #: If it is a backup from volume, it will be the same as created_at
    #: for a backup. If it is a backup from a snapshot,
    #: it will be the same as created_at for the snapshot.
    data_timestamp = resource.Body('data_timestamp')
    #: backup description
    description = resource.Body("description")
    #: Backup fail reason
    fail_reason = resource.Body("fail_reason")
    #: Force backup
    force = resource.Body("force", type=bool)
    #: has_dependent_backups
    #: If this value is true, there are other backups depending on this backup.
    has_dependent_backups = resource.Body('has_dependent_backups', type=bool)
    #: Indicates whether the backup mode is incremental.
    #: If this value is true, the backup mode is incremental.
    #: If this value is false, the backup mode is full.
    is_incremental = resource.Body("is_incremental", type=bool)
    #: A list of links associated with this volume. *Type: list*
    links = resource.Body("links", type=list)
    #: The backup metadata. New in version 3.43
    metadata = resource.Body('metadata', type=dict)
    #: backup name
    name = resource.Body("name")
    #: backup object count
    object_count = resource.Body("object_count", type=int)
    #: The UUID of the owning project.
    #: New in version 3.18
    project_id = resource.Body('os-backup-project-attr:project_id')
    #: The size of the volume, in gibibytes (GiB).
    size = resource.Body("size", type=int)
    #: The UUID of the source volume snapshot.
    snapshot_id = resource.Body("snapshot_id")
    #: backup status
    #: values: creating, available, deleting, error, restoring, error_restoring
    status = resource.Body("status")
    #: The date and time when the resource was updated.
    updated_at = resource.Body("updated_at")
    #: The UUID of the project owner. New in 3.56
    user_id = resource.Body('user_id')
    #: The UUID of the volume.
    volume_id = resource.Body("volume_id")

    def restore(self, session, volume_id=None, name=None):
        """Restore current backup to volume

        :param session: openstack session
        :param volume_id: The ID of the volume to restore the backup to.
        :param name: The name for new volume creation to restore.
        :return: Updated backup instance
        """
        url = utils.urljoin(self.base_path, self.id, "restore")
        body = {'restore': {}}
        if volume_id:
            body['restore']['volume_id'] = volume_id
        if name:
            body['restore']['name'] = name
        if not (volume_id or name):
            raise exceptions.SDKException('Either of `name` or `volume_id`'
                                          ' must be specified.')
        response = session.post(url,
                                json=body)
        self._translate_response(response, has_body=False)
        return self


BackupDetail = Backup
