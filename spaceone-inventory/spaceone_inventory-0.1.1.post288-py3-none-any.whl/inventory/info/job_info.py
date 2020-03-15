# -*- coding: utf-8 -*-
import functools

from spaceone.api.inventory.v1 import collector_pb2, job_pb2
from spaceone.core.pygrpc.message_type import *
from spaceone.inventory.model.job_model import Job
from spaceone.inventory.info.collector_info import CollectorInfo

__all__ = ['JobInfo', 'JobsInfo']


def JobInfo(job_vo: Job, minimal=False):
    info = {
        'job_id': job_vo.job_id,
        'created_at': change_timestamp_type(job_vo.created_at),
        'finished_at': change_timestamp_type(job_vo.finished_at),
        'state': job_vo.state
    }

    if not minimal:
        info.update({
            'collector_info': CollectorInfo(job_vo.collector, minimal=True),
            'created_count': job_vo.created_count,
            'updated_count': job_vo.updated_count,
            'collected_resources': job_vo.collected_resources
        })

    return collector_pb2.JobInfo(**info)

def JobsInfo(vos, total_count, **kwargs):
    return job_pb2.JobsInfo(results=list(map(functools.partial(JobInfo, **kwargs), vos)), total_count=total_count) 
