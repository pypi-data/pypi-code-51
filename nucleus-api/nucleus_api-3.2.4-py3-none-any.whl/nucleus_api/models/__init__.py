# coding: utf-8

# flake8: noqa
"""
    Nucleus API

    Nucleus text analytics APIs from SumUp Analytics. Example and documentation: https://www.sumup.ai/apis/#nucleus-documentation  # noqa: E501

    OpenAPI spec version: v3.2.4
    Contact: info@sumup.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from nucleus_api.models.admin_add_user_model import AdminAddUserModel
from nucleus_api.models.admin_add_user_resp_model import AdminAddUserRespModel
from nucleus_api.models.admin_delete_user_model import AdminDeleteUserModel
from nucleus_api.models.admin_delete_user_resp_model import AdminDeleteUserRespModel
from nucleus_api.models.admin_list_model import AdminListModel
from nucleus_api.models.admin_list_resp_model import AdminListRespModel
from nucleus_api.models.admin_manage_dataset_model import AdminManageDatasetModel
from nucleus_api.models.admin_manage_dataset_resp_model import AdminManageDatasetRespModel
from nucleus_api.models.admin_update_user_model import AdminUpdateUserModel
from nucleus_api.models.admin_update_user_resp_model import AdminUpdateUserRespModel
from nucleus_api.models.api_call import ApiCall
from nucleus_api.models.append_json_resp_model import AppendJsonRespModel
from nucleus_api.models.appendjsonparams import Appendjsonparams
from nucleus_api.models.author_connect_l1_resp_model import AuthorConnectL1RespModel
from nucleus_api.models.author_connect_l2_resp_model import AuthorConnectL2RespModel
from nucleus_api.models.author_connect_resp_model import AuthorConnectRespModel
from nucleus_api.models.author_connection import AuthorConnection
from nucleus_api.models.available_filings_response_model import AvailableFilingsResponseModel
from nucleus_api.models.bulk_insert_params import BulkInsertParams
from nucleus_api.models.bulk_insert_resp_model import BulkInsertRespModel
from nucleus_api.models.create_sec_dataset_response_model import CreateSecDatasetResponseModel
from nucleus_api.models.custom_tracker_l1_resp_model import CustomTrackerL1RespModel
from nucleus_api.models.custom_tracker_model import CustomTrackerModel
from nucleus_api.models.custom_tracker_resp_model import CustomTrackerRespModel
from nucleus_api.models.dataset_info import DatasetInfo
from nucleus_api.models.dataset_info_model import DatasetInfoModel
from nucleus_api.models.dataset_info_resp_model import DatasetInfoRespModel
from nucleus_api.models.dataset_model import DatasetModel
from nucleus_api.models.dataset_tagging import DatasetTagging
from nucleus_api.models.dataset_tagging_l1_resp_model import DatasetTaggingL1RespModel
from nucleus_api.models.dataset_tagging_resp_model import DatasetTaggingRespModel
from nucleus_api.models.delete_dataset_model import DeleteDatasetModel
from nucleus_api.models.delete_dataset_resp_model import DeleteDatasetRespModel
from nucleus_api.models.delete_document_model import DeleteDocumentModel
from nucleus_api.models.delete_document_resp_model import DeleteDocumentRespModel
from nucleus_api.models.delete_filter_model import DeleteFilterModel
from nucleus_api.models.delete_filter_resp_model import DeleteFilterRespModel
from nucleus_api.models.doc_classify_l1_resp_model import DocClassifyL1RespModel
from nucleus_api.models.doc_classify_l2_dr_resp_model import DocClassifyL2DRRespModel
from nucleus_api.models.doc_classify_l2_pm_resp_model import DocClassifyL2PMRespModel
from nucleus_api.models.doc_classify_model import DocClassifyModel
from nucleus_api.models.doc_classify_resp_model import DocClassifyRespModel
from nucleus_api.models.doc_display import DocDisplay
from nucleus_api.models.doc_display_l1_resp_model import DocDisplayL1RespModel
from nucleus_api.models.doc_display_resp_model import DocDisplayRespModel
from nucleus_api.models.doc_info import DocInfo
from nucleus_api.models.doc_info_resp_model import DocInfoRespModel
from nucleus_api.models.document import Document
from nucleus_api.models.document_contrast_summary_l1_model import DocumentContrastSummaryL1Model
from nucleus_api.models.document_contrast_summary_l2_model import DocumentContrastSummaryL2Model
from nucleus_api.models.document_contrast_summary_model import DocumentContrastSummaryModel
from nucleus_api.models.document_contrast_summary_resp_model import DocumentContrastSummaryRespModel
from nucleus_api.models.document_new_words_l1_model import DocumentNewWordsL1Model
from nucleus_api.models.document_new_words_model import DocumentNewWordsModel
from nucleus_api.models.document_new_words_resp_model import DocumentNewWordsRespModel
from nucleus_api.models.document_novelty_l1_model import DocumentNoveltyL1Model
from nucleus_api.models.document_novelty_model import DocumentNoveltyModel
from nucleus_api.models.document_novelty_resp_model import DocumentNoveltyRespModel
from nucleus_api.models.document_recommend_l1_resp_model import DocumentRecommendL1RespModel
from nucleus_api.models.document_recommend_l2_resp_model import DocumentRecommendL2RespModel
from nucleus_api.models.document_recommend_model import DocumentRecommendModel
from nucleus_api.models.document_recommend_resp_model import DocumentRecommendRespModel
from nucleus_api.models.document_sentiment_l1_model import DocumentSentimentL1Model
from nucleus_api.models.document_sentiment_model import DocumentSentimentModel
from nucleus_api.models.document_sentiment_resp_model import DocumentSentimentRespModel
from nucleus_api.models.document_summary_l1_model import DocumentSummaryL1Model
from nucleus_api.models.document_summary_l2_model import DocumentSummaryL2Model
from nucleus_api.models.document_summary_model import DocumentSummaryModel
from nucleus_api.models.document_summary_resp_model import DocumentSummaryRespModel
from nucleus_api.models.edgar_available_fields import EdgarAvailableFields
from nucleus_api.models.edgar_fields import EdgarFields
from nucleus_api.models.edgar_query import EdgarQuery
from nucleus_api.models.example_job_inner_response import ExampleJobInnerResponse
from nucleus_api.models.example_job_response import ExampleJobResponse
from nucleus_api.models.file_property_model import FilePropertyModel
from nucleus_api.models.filter_model import FilterModel
from nucleus_api.models.job_resp_model import JobRespModel
from nucleus_api.models.job_status_resp_model import JobStatusRespModel
from nucleus_api.models.json_property_model import JsonPropertyModel
from nucleus_api.models.key_authors_l1_resp_model import KeyAuthorsL1RespModel
from nucleus_api.models.key_authors_l2_resp_model import KeyAuthorsL2RespModel
from nucleus_api.models.key_authors_model import KeyAuthorsModel
from nucleus_api.models.key_authors_resp_model import KeyAuthorsRespModel
from nucleus_api.models.legacy_response_model import LegacyResponseModel
from nucleus_api.models.list_datasets_model import ListDatasetsModel
from nucleus_api.models.list_filters_model import ListFiltersModel
from nucleus_api.models.metadata_autocomplete import MetadataAutocomplete
from nucleus_api.models.metadata_autocomplete_resp_model import MetadataAutocompleteRespModel
from nucleus_api.models.metadata_histogram import MetadataHistogram
from nucleus_api.models.nested_doc_info_model import NestedDocInfoModel
from nucleus_api.models.nested_topic_consensus_model import NestedTopicConsensusModel
from nucleus_api.models.nested_topic_consensus_transfer_model import NestedTopicConsensusTransferModel
from nucleus_api.models.nested_topic_sentiment_transfer_model import NestedTopicSentimentTransferModel
from nucleus_api.models.post_user_resp_model import PostUserRespModel
from nucleus_api.models.rename_dataset_model import RenameDatasetModel
from nucleus_api.models.rename_dataset_resp_model import RenameDatasetRespModel
from nucleus_api.models.save_filter_model import SaveFilterModel
from nucleus_api.models.save_filter_resp_model import SaveFilterRespModel
from nucleus_api.models.smart_alerts_l1_resp_model import SmartAlertsL1RespModel
from nucleus_api.models.smart_alerts_l2_resp_model import SmartAlertsL2RespModel
from nucleus_api.models.smart_alerts_model import SmartAlertsModel
from nucleus_api.models.smart_alerts_resp_model import SmartAlertsRespModel
from nucleus_api.models.topic_consensus_model import TopicConsensusModel
from nucleus_api.models.topic_consensus_resp_model import TopicConsensusRespModel
from nucleus_api.models.topic_consensus_transfer_model import TopicConsensusTransferModel
from nucleus_api.models.topic_consensus_transfer_resp_model import TopicConsensusTransferRespModel
from nucleus_api.models.topic_contrast_l1_resp_model import TopicContrastL1RespModel
from nucleus_api.models.topic_contrast_l21_resp_model import TopicContrastL21RespModel
from nucleus_api.models.topic_contrast_l22_resp_model import TopicContrastL22RespModel
from nucleus_api.models.topic_contrast_model import TopicContrastModel
from nucleus_api.models.topic_contrast_resp_model import TopicContrastRespModel
from nucleus_api.models.topic_delta_l1_resp_model import TopicDeltaL1RespModel
from nucleus_api.models.topic_delta_l2_resp_model import TopicDeltaL2RespModel
from nucleus_api.models.topic_delta_model import TopicDeltaModel
from nucleus_api.models.topic_delta_resp_model import TopicDeltaRespModel
from nucleus_api.models.topic_history_l1_resp_model import TopicHistoryL1RespModel
from nucleus_api.models.topic_history_model import TopicHistoryModel
from nucleus_api.models.topic_history_resp_model import TopicHistoryRespModel
from nucleus_api.models.topic_l1_resp_model import TopicL1RespModel
from nucleus_api.models.topic_l2_resp_model import TopicL2RespModel
from nucleus_api.models.topic_resp_model import TopicRespModel
from nucleus_api.models.topic_sentiment_l1_resp_model import TopicSentimentL1RespModel
from nucleus_api.models.topic_sentiment_model import TopicSentimentModel
from nucleus_api.models.topic_sentiment_resp_model import TopicSentimentRespModel
from nucleus_api.models.topic_sentiment_transfer_model import TopicSentimentTransferModel
from nucleus_api.models.topic_sentiment_transfer_resp_model import TopicSentimentTransferRespModel
from nucleus_api.models.topic_summary_l1_resp_model import TopicSummaryL1RespModel
from nucleus_api.models.topic_summary_l2_resp_model import TopicSummaryL2RespModel
from nucleus_api.models.topic_summary_model import TopicSummaryModel
from nucleus_api.models.topic_summary_resp_model import TopicSummaryRespModel
from nucleus_api.models.topic_transfer_l1_resp_model import TopicTransferL1RespModel
from nucleus_api.models.topic_transfer_l2_resp_model import TopicTransferL2RespModel
from nucleus_api.models.topic_transfer_model import TopicTransferModel
from nucleus_api.models.topic_transfer_resp_model import TopicTransferRespModel
from nucleus_api.models.topics import Topics
from nucleus_api.models.update_dataset_metadata_model import UpdateDatasetMetadataModel
from nucleus_api.models.update_dataset_metadata_resp_model import UpdateDatasetMetadataRespModel
from nucleus_api.models.upload_file_resp_model import UploadFileRespModel
from nucleus_api.models.upload_url_model import UploadURLModel
from nucleus_api.models.upload_url_resp_model import UploadUrlRespModel
from nucleus_api.models.url_property_model import UrlPropertyModel
from nucleus_api.models.user import User
from nucleus_api.models.user_model import UserModel
