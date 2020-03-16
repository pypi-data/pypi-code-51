# coding: utf-8

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 11.2.1-rc.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


## NOTE: This file is auto generated by the swagger code generator program.
## Do not edit the file manually.

import pprint
import re  # noqa: F401

import six

from flywheel.models.analysis_output import AnalysisOutput  # noqa: F401,E501
from flywheel.models.common_info import CommonInfo  # noqa: F401,E501
from flywheel.models.container_parents import ContainerParents  # noqa: F401,E501
from flywheel.models.container_reference import ContainerReference  # noqa: F401,E501
from flywheel.models.file_entry import FileEntry  # noqa: F401,E501
from flywheel.models.gear_info import GearInfo  # noqa: F401,E501
from flywheel.models.job import Job  # noqa: F401,E501
from flywheel.models.note import Note  # noqa: F401,E501
from flywheel.models.resolver_node import ResolverNode  # noqa: F401,E501

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.

from .mixins import AnalysisMixin

class ResolverAnalysisNode(AnalysisMixin):

    swagger_types = {
        'id': 'str',
        'inputs': 'list[FileEntry]',
        'files': 'list[FileEntry]',
        'job': 'Job',
        'gear_info': 'GearInfo',
        'notes': 'list[Note]',
        'tags': 'list[str]',
        'info': 'CommonInfo',
        'description': 'str',
        'label': 'str',
        'parent': 'ContainerReference',
        'parents': 'ContainerParents',
        'created': 'datetime',
        'modified': 'datetime',
        'revision': 'int'
    }

    attribute_map = {
        'id': '_id',
        'inputs': 'inputs',
        'files': 'files',
        'job': 'job',
        'gear_info': 'gear_info',
        'notes': 'notes',
        'tags': 'tags',
        'info': 'info',
        'description': 'description',
        'label': 'label',
        'parent': 'parent',
        'parents': 'parents',
        'created': 'created',
        'modified': 'modified',
        'revision': 'revision'
    }

    rattribute_map = {
        '_id': 'id',
        'inputs': 'inputs',
        'files': 'files',
        'job': 'job',
        'gear_info': 'gear_info',
        'notes': 'notes',
        'tags': 'tags',
        'info': 'info',
        'description': 'description',
        'label': 'label',
        'parent': 'parent',
        'parents': 'parents',
        'created': 'created',
        'modified': 'modified',
        'revision': 'revision'
    }

    def __init__(self, id=None, inputs=None, files=None, job=None, gear_info=None, notes=None, tags=None, info=None, description=None, label=None, parent=None, parents=None, created=None, modified=None, revision=None):  # noqa: E501
        """ResolverAnalysisNode - a model defined in Swagger"""
        super(ResolverAnalysisNode, self).__init__()

        self._id = None
        self._inputs = None
        self._files = None
        self._job = None
        self._gear_info = None
        self._notes = None
        self._tags = None
        self._info = None
        self._description = None
        self._label = None
        self._parent = None
        self._parents = None
        self._created = None
        self._modified = None
        self._revision = None
        self.discriminator = None
        self.alt_discriminator = None

        self.id = id
        if inputs is not None:
            self.inputs = inputs
        if files is not None:
            self.files = files
        if job is not None:
            self.job = job
        if gear_info is not None:
            self.gear_info = gear_info
        if notes is not None:
            self.notes = notes
        if tags is not None:
            self.tags = tags
        if info is not None:
            self.info = info
        if description is not None:
            self.description = description
        self.label = label
        if parent is not None:
            self.parent = parent
        if parents is not None:
            self.parents = parents
        self.created = created
        self.modified = modified
        if revision is not None:
            self.revision = revision

    @property
    def id(self):
        """Gets the id of this ResolverAnalysisNode.

        Unique database ID

        :return: The id of this ResolverAnalysisNode.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResolverAnalysisNode.

        Unique database ID

        :param id: The id of this ResolverAnalysisNode.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def inputs(self):
        """Gets the inputs of this ResolverAnalysisNode.


        :return: The inputs of this ResolverAnalysisNode.
        :rtype: list[FileEntry]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this ResolverAnalysisNode.


        :param inputs: The inputs of this ResolverAnalysisNode.  # noqa: E501
        :type: list[FileEntry]
        """

        self._inputs = inputs

    @property
    def files(self):
        """Gets the files of this ResolverAnalysisNode.


        :return: The files of this ResolverAnalysisNode.
        :rtype: list[FileEntry]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this ResolverAnalysisNode.


        :param files: The files of this ResolverAnalysisNode.  # noqa: E501
        :type: list[FileEntry]
        """

        self._files = files

    @property
    def job(self):
        """Gets the job of this ResolverAnalysisNode.


        :return: The job of this ResolverAnalysisNode.
        :rtype: Job
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this ResolverAnalysisNode.


        :param job: The job of this ResolverAnalysisNode.  # noqa: E501
        :type: Job
        """

        self._job = job

    @property
    def gear_info(self):
        """Gets the gear_info of this ResolverAnalysisNode.


        :return: The gear_info of this ResolverAnalysisNode.
        :rtype: GearInfo
        """
        return self._gear_info

    @gear_info.setter
    def gear_info(self, gear_info):
        """Sets the gear_info of this ResolverAnalysisNode.


        :param gear_info: The gear_info of this ResolverAnalysisNode.  # noqa: E501
        :type: GearInfo
        """

        self._gear_info = gear_info

    @property
    def notes(self):
        """Gets the notes of this ResolverAnalysisNode.


        :return: The notes of this ResolverAnalysisNode.
        :rtype: list[Note]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this ResolverAnalysisNode.


        :param notes: The notes of this ResolverAnalysisNode.  # noqa: E501
        :type: list[Note]
        """

        self._notes = notes

    @property
    def tags(self):
        """Gets the tags of this ResolverAnalysisNode.

        Array of application-specific tags

        :return: The tags of this ResolverAnalysisNode.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ResolverAnalysisNode.

        Array of application-specific tags

        :param tags: The tags of this ResolverAnalysisNode.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def info(self):
        """Gets the info of this ResolverAnalysisNode.


        :return: The info of this ResolverAnalysisNode.
        :rtype: CommonInfo
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this ResolverAnalysisNode.


        :param info: The info of this ResolverAnalysisNode.  # noqa: E501
        :type: CommonInfo
        """

        self._info = info

    @property
    def description(self):
        """Gets the description of this ResolverAnalysisNode.


        :return: The description of this ResolverAnalysisNode.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ResolverAnalysisNode.


        :param description: The description of this ResolverAnalysisNode.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def label(self):
        """Gets the label of this ResolverAnalysisNode.

        Application-specific label

        :return: The label of this ResolverAnalysisNode.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ResolverAnalysisNode.

        Application-specific label

        :param label: The label of this ResolverAnalysisNode.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def parent(self):
        """Gets the parent of this ResolverAnalysisNode.


        :return: The parent of this ResolverAnalysisNode.
        :rtype: ContainerReference
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this ResolverAnalysisNode.


        :param parent: The parent of this ResolverAnalysisNode.  # noqa: E501
        :type: ContainerReference
        """

        self._parent = parent

    @property
    def parents(self):
        """Gets the parents of this ResolverAnalysisNode.


        :return: The parents of this ResolverAnalysisNode.
        :rtype: ContainerParents
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """Sets the parents of this ResolverAnalysisNode.


        :param parents: The parents of this ResolverAnalysisNode.  # noqa: E501
        :type: ContainerParents
        """

        self._parents = parents

    @property
    def created(self):
        """Gets the created of this ResolverAnalysisNode.

        Creation time (automatically set)

        :return: The created of this ResolverAnalysisNode.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ResolverAnalysisNode.

        Creation time (automatically set)

        :param created: The created of this ResolverAnalysisNode.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this ResolverAnalysisNode.

        Last modification time (automatically updated)

        :return: The modified of this ResolverAnalysisNode.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this ResolverAnalysisNode.

        Last modification time (automatically updated)

        :param modified: The modified of this ResolverAnalysisNode.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def revision(self):
        """Gets the revision of this ResolverAnalysisNode.

        An incremental document revision number

        :return: The revision of this ResolverAnalysisNode.
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this ResolverAnalysisNode.

        An incremental document revision number

        :param revision: The revision of this ResolverAnalysisNode.  # noqa: E501
        :type: int
        """

        self._revision = revision


    @staticmethod
    def positional_to_model(value):
        """Converts a positional argument to a model value"""
        return value

    def return_value(self):
        """Unwraps return value from model"""
        return self

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResolverAnalysisNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    # Container emulation
    def __getitem__(self, key):
        """Returns the value of key"""
        key = self._map_key(key)
        return getattr(self, key)

    def __setitem__(self, key, value):
        """Sets the value of key"""
        key = self._map_key(key)
        setattr(self, key, value)

    def __contains__(self, key):
        """Checks if the given value is a key in this object"""
        key = self._map_key(key, raise_on_error=False)
        return key is not None

    def keys(self):
        """Returns the list of json properties in the object"""
        return self.__class__.rattribute_map.keys()

    def values(self):
        """Returns the list of values in the object"""
        for key in self.__class__.attribute_map.keys():
            yield getattr(self, key)

    def items(self):
        """Returns the list of json property to value mapping"""
        for key, prop in self.__class__.rattribute_map.items():
            yield key, getattr(self, prop)

    def get(self, key, default=None):
        """Get the value of the provided json property, or default"""
        key = self._map_key(key, raise_on_error=False)
        if key:
            return getattr(self, key, default)
        return default

    def _map_key(self, key, raise_on_error=True):
        result = self.__class__.rattribute_map.get(key)
        if result is None:
            if raise_on_error:
                raise AttributeError('Invalid attribute name: {}'.format(key))
            return None
        return '_' + result
