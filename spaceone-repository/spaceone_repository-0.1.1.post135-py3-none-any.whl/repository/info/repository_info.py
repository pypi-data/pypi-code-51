# -*- coding: utf-8 -*-

__all__ = ['RepositoryInfo','RepositoriesInfo']

import functools
from spaceone.api.repository.v1 import repository_pb2
from spaceone.core.pygrpc.message_type import *
from spaceone.repository.model.repository_model import Repository

def RepositoryInfo(repository_vo: Repository, minimal=False):
    info = {
        'repository_id': repository_vo.repository_id,
        'name': repository_vo.name,
        'repository_type': repository_vo.repository_type
    }
    if minimal is False:
        info.update({
                'endpoint': repository_vo.endpoint,
                'version': repository_vo.version,
                'credential_id': repository_vo.credential_id,
                'created_at': change_timestamp_type(repository_vo.created_at)
                })

    return repository_pb2.RepositoryInfo(**info)

def RepositoriesInfo(repo_vos, total_count):
    results = list(map(functools.partial(RepositoryInfo), repo_vos))
    return repository_pb2.RepositoriesInfo(results=results, total_count=total_count)
