# -*- coding: utf-8 -*-
from mongoengine import *
from spaceone.core.model.mongo_model import MongoModel

from spaceone.inventory.model.collection_info_model import CollectionInfo


class DataSource(EmbeddedDocument):
    name = StringField(max_length=255)
    key = StringField()
    view_type = StringField(max_length=40)
    view_option = DictField()


class CloudServiceType(MongoModel):
    cloud_service_type_id = StringField(max_length=40, generate_id='cloud-svc-type', unique=True)
    name = StringField(max_length=255, unique_with=['provider', 'group', 'domain_id'])
    provider = StringField(max_length=255)
    group = StringField(max_length=255)
    labels = ListField(StringField(max_length=255))
    data_source = ListField(EmbeddedDocumentField(DataSource))
    tags = DictField()
    domain_id = StringField(max_length=40)
    collection_info = EmbeddedDocumentField(CollectionInfo, default=CollectionInfo)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    meta = {
        'updatable_fields': [
            'data_source',
            'labels',
            'tags',
            'collection_info'
        ],
        'exact_fields': [
            'cloud_service_type_id',
            'domain_id',
            'collection_info.state'
        ],
        'minimal_fields': [
            'cloud_service_type_id',
            'name',
            'provider',
            'group',
            'collection_info.state'
        ],
        'ordering': [
            'name'
        ],
        'indexes': [
            'cloud_service_type_id',
            'name',
            'provider',
            'group',
            'domain_id',
            'collection_info.state'
        ]
    }
