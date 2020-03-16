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

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.


class ReportDailyUsageEntry(object):

    swagger_types = {
        'year': 'int',
        'month': 'int',
        'day': 'int',
        'group': 'str',
        'project': 'str',
        'project_label': 'str',
        'session_count': 'int',
        'center_job_count': 'int',
        'group_job_count': 'int',
        'center_compute_ms': 'int',
        'group_compute_ms': 'int',
        'center_storage_bytes': 'int',
        'group_storage_bytes': 'int'
    }

    attribute_map = {
        'year': 'year',
        'month': 'month',
        'day': 'day',
        'group': 'group',
        'project': 'project',
        'project_label': 'project_label',
        'session_count': 'session_count',
        'center_job_count': 'center_job_count',
        'group_job_count': 'group_job_count',
        'center_compute_ms': 'center_compute_ms',
        'group_compute_ms': 'group_compute_ms',
        'center_storage_bytes': 'center_storage_bytes',
        'group_storage_bytes': 'group_storage_bytes'
    }

    rattribute_map = {
        'year': 'year',
        'month': 'month',
        'day': 'day',
        'group': 'group',
        'project': 'project',
        'project_label': 'project_label',
        'session_count': 'session_count',
        'center_job_count': 'center_job_count',
        'group_job_count': 'group_job_count',
        'center_compute_ms': 'center_compute_ms',
        'group_compute_ms': 'group_compute_ms',
        'center_storage_bytes': 'center_storage_bytes',
        'group_storage_bytes': 'group_storage_bytes'
    }

    def __init__(self, year=None, month=None, day=None, group=None, project=None, project_label=None, session_count=None, center_job_count=None, group_job_count=None, center_compute_ms=None, group_compute_ms=None, center_storage_bytes=None, group_storage_bytes=None):  # noqa: E501
        """ReportDailyUsageEntry - a model defined in Swagger"""
        super(ReportDailyUsageEntry, self).__init__()

        self._year = None
        self._month = None
        self._day = None
        self._group = None
        self._project = None
        self._project_label = None
        self._session_count = None
        self._center_job_count = None
        self._group_job_count = None
        self._center_compute_ms = None
        self._group_compute_ms = None
        self._center_storage_bytes = None
        self._group_storage_bytes = None
        self.discriminator = None
        self.alt_discriminator = None

        self.year = year
        self.month = month
        self.day = day
        self.group = group
        self.project = project
        self.project_label = project_label
        self.session_count = session_count
        self.center_job_count = center_job_count
        self.group_job_count = group_job_count
        self.center_compute_ms = center_compute_ms
        self.group_compute_ms = group_compute_ms
        self.center_storage_bytes = center_storage_bytes
        self.group_storage_bytes = group_storage_bytes

    @property
    def year(self):
        """Gets the year of this ReportDailyUsageEntry.

        The year that this report row represents

        :return: The year of this ReportDailyUsageEntry.
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this ReportDailyUsageEntry.

        The year that this report row represents

        :param year: The year of this ReportDailyUsageEntry.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def month(self):
        """Gets the month of this ReportDailyUsageEntry.

        The month that this report row represents

        :return: The month of this ReportDailyUsageEntry.
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this ReportDailyUsageEntry.

        The month that this report row represents

        :param month: The month of this ReportDailyUsageEntry.  # noqa: E501
        :type: int
        """

        self._month = month

    @property
    def day(self):
        """Gets the day of this ReportDailyUsageEntry.

        The day that this report row represents

        :return: The day of this ReportDailyUsageEntry.
        :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this ReportDailyUsageEntry.

        The day that this report row represents

        :param day: The day of this ReportDailyUsageEntry.  # noqa: E501
        :type: int
        """

        self._day = day

    @property
    def group(self):
        """Gets the group of this ReportDailyUsageEntry.

        The group label

        :return: The group of this ReportDailyUsageEntry.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ReportDailyUsageEntry.

        The group label

        :param group: The group of this ReportDailyUsageEntry.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def project(self):
        """Gets the project of this ReportDailyUsageEntry.

        Unique database ID

        :return: The project of this ReportDailyUsageEntry.
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ReportDailyUsageEntry.

        Unique database ID

        :param project: The project of this ReportDailyUsageEntry.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def project_label(self):
        """Gets the project_label of this ReportDailyUsageEntry.

        Application-specific label

        :return: The project_label of this ReportDailyUsageEntry.
        :rtype: str
        """
        return self._project_label

    @project_label.setter
    def project_label(self, project_label):
        """Sets the project_label of this ReportDailyUsageEntry.

        Application-specific label

        :param project_label: The project_label of this ReportDailyUsageEntry.  # noqa: E501
        :type: str
        """

        self._project_label = project_label

    @property
    def session_count(self):
        """Gets the session_count of this ReportDailyUsageEntry.

        The number of sessions that existed at the last collection time

        :return: The session_count of this ReportDailyUsageEntry.
        :rtype: int
        """
        return self._session_count

    @session_count.setter
    def session_count(self, session_count):
        """Sets the session_count of this ReportDailyUsageEntry.

        The number of sessions that existed at the last collection time

        :param session_count: The session_count of this ReportDailyUsageEntry.  # noqa: E501
        :type: int
        """

        self._session_count = session_count

    @property
    def center_job_count(self):
        """Gets the center_job_count of this ReportDailyUsageEntry.

        The number of jobs that completed during the time frame that are billable to the center

        :return: The center_job_count of this ReportDailyUsageEntry.
        :rtype: int
        """
        return self._center_job_count

    @center_job_count.setter
    def center_job_count(self, center_job_count):
        """Sets the center_job_count of this ReportDailyUsageEntry.

        The number of jobs that completed during the time frame that are billable to the center

        :param center_job_count: The center_job_count of this ReportDailyUsageEntry.  # noqa: E501
        :type: int
        """

        self._center_job_count = center_job_count

    @property
    def group_job_count(self):
        """Gets the group_job_count of this ReportDailyUsageEntry.

        The number of jobs that completed during the time frame that are billable to the group

        :return: The group_job_count of this ReportDailyUsageEntry.
        :rtype: int
        """
        return self._group_job_count

    @group_job_count.setter
    def group_job_count(self, group_job_count):
        """Sets the group_job_count of this ReportDailyUsageEntry.

        The number of jobs that completed during the time frame that are billable to the group

        :param group_job_count: The group_job_count of this ReportDailyUsageEntry.  # noqa: E501
        :type: int
        """

        self._group_job_count = group_job_count

    @property
    def center_compute_ms(self):
        """Gets the center_compute_ms of this ReportDailyUsageEntry.

        The compute time of jobs completed during the time frame, billable to the center

        :return: The center_compute_ms of this ReportDailyUsageEntry.
        :rtype: int
        """
        return self._center_compute_ms

    @center_compute_ms.setter
    def center_compute_ms(self, center_compute_ms):
        """Sets the center_compute_ms of this ReportDailyUsageEntry.

        The compute time of jobs completed during the time frame, billable to the center

        :param center_compute_ms: The center_compute_ms of this ReportDailyUsageEntry.  # noqa: E501
        :type: int
        """

        self._center_compute_ms = center_compute_ms

    @property
    def group_compute_ms(self):
        """Gets the group_compute_ms of this ReportDailyUsageEntry.

        The compute time of jobs completed during the time frame, billable to the group

        :return: The group_compute_ms of this ReportDailyUsageEntry.
        :rtype: int
        """
        return self._group_compute_ms

    @group_compute_ms.setter
    def group_compute_ms(self, group_compute_ms):
        """Sets the group_compute_ms of this ReportDailyUsageEntry.

        The compute time of jobs completed during the time frame, billable to the group

        :param group_compute_ms: The group_compute_ms of this ReportDailyUsageEntry.  # noqa: E501
        :type: int
        """

        self._group_compute_ms = group_compute_ms

    @property
    def center_storage_bytes(self):
        """Gets the center_storage_bytes of this ReportDailyUsageEntry.

        The total storage used on this day, billable to the center

        :return: The center_storage_bytes of this ReportDailyUsageEntry.
        :rtype: int
        """
        return self._center_storage_bytes

    @center_storage_bytes.setter
    def center_storage_bytes(self, center_storage_bytes):
        """Sets the center_storage_bytes of this ReportDailyUsageEntry.

        The total storage used on this day, billable to the center

        :param center_storage_bytes: The center_storage_bytes of this ReportDailyUsageEntry.  # noqa: E501
        :type: int
        """

        self._center_storage_bytes = center_storage_bytes

    @property
    def group_storage_bytes(self):
        """Gets the group_storage_bytes of this ReportDailyUsageEntry.

        The total storage used on this day, billable to the group

        :return: The group_storage_bytes of this ReportDailyUsageEntry.
        :rtype: int
        """
        return self._group_storage_bytes

    @group_storage_bytes.setter
    def group_storage_bytes(self, group_storage_bytes):
        """Sets the group_storage_bytes of this ReportDailyUsageEntry.

        The total storage used on this day, billable to the group

        :param group_storage_bytes: The group_storage_bytes of this ReportDailyUsageEntry.  # noqa: E501
        :type: int
        """

        self._group_storage_bytes = group_storage_bytes


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
        if not isinstance(other, ReportDailyUsageEntry):
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
