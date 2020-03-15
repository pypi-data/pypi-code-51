# -*- coding: utf-8 -*-
from spaceone.core.service import *
from spaceone.inventory.manager.job_manager import JobManager


@authentication_handler
@authorization_handler
@event_handler
class JobService(BaseService):

    def __init__(self, metadata):
        super().__init__(metadata)
        self.job_mgr: JobManager = self.locator.get_manager('JobManager')

    @transaction
    @check_required(['domain_id'])
    @append_query_filter(['job_id', 'state', 'collect_mode', 'collector_id', 'resource_type', 'resource_id', 'domain_id'])
    def list(self, params):
        """
        Args:
            params (dict): {
                    'job_id': 'str',
                    'state': 'str',
                    'collect_mode': 'str',
                    'collector_id': 'dict',
                    'resource_type': 'str',
                    'resource_id': 'str',
                    'domain_id  ': 'str',
                    'query': 'dict'
                }

        Returns:
            results (list)
            total_count (int)

        """

        return self.job_mgr.list_jobs(params.get('query', {}))

