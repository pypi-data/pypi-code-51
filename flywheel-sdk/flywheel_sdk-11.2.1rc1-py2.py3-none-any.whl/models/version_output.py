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


class VersionOutput(object):

    swagger_types = {
        'id': 'str',
        'applied_fixes': 'dict(str, str)',
        'cli_version': 'str',
        'database': 'int',
        'flywheel_release': 'str',
        'release': 'str'
    }

    attribute_map = {
        'id': '_id',
        'applied_fixes': 'applied_fixes',
        'cli_version': 'cli_version',
        'database': 'database',
        'flywheel_release': 'flywheel_release',
        'release': 'release'
    }

    rattribute_map = {
        '_id': 'id',
        'applied_fixes': 'applied_fixes',
        'cli_version': 'cli_version',
        'database': 'database',
        'flywheel_release': 'flywheel_release',
        'release': 'release'
    }

    def __init__(self, id=None, applied_fixes=None, cli_version=None, database=None, flywheel_release=None, release=None):  # noqa: E501
        """VersionOutput - a model defined in Swagger"""
        super(VersionOutput, self).__init__()

        self._id = None
        self._applied_fixes = None
        self._cli_version = None
        self._database = None
        self._flywheel_release = None
        self._release = None
        self.discriminator = None
        self.alt_discriminator = None

        self.id = id
        if applied_fixes is not None:
            self.applied_fixes = applied_fixes
        if cli_version is not None:
            self.cli_version = cli_version
        self.database = database
        if flywheel_release is not None:
            self.flywheel_release = flywheel_release
        if release is not None:
            self.release = release

    @property
    def id(self):
        """Gets the id of this VersionOutput.


        :return: The id of this VersionOutput.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VersionOutput.


        :param id: The id of this VersionOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def applied_fixes(self):
        """Gets the applied_fixes of this VersionOutput.

        Collection of applied database fixes

        :return: The applied_fixes of this VersionOutput.
        :rtype: dict(str, str)
        """
        return self._applied_fixes

    @applied_fixes.setter
    def applied_fixes(self, applied_fixes):
        """Sets the applied_fixes of this VersionOutput.

        Collection of applied database fixes

        :param applied_fixes: The applied_fixes of this VersionOutput.  # noqa: E501
        :type: dict(str, str)
        """

        self._applied_fixes = applied_fixes

    @property
    def cli_version(self):
        """Gets the cli_version of this VersionOutput.

        Compatible CLI version for this server as informed by the installation recipe.env

        :return: The cli_version of this VersionOutput.
        :rtype: str
        """
        return self._cli_version

    @cli_version.setter
    def cli_version(self, cli_version):
        """Sets the cli_version of this VersionOutput.

        Compatible CLI version for this server as informed by the installation recipe.env

        :param cli_version: The cli_version of this VersionOutput.  # noqa: E501
        :type: str
        """

        self._cli_version = cli_version

    @property
    def database(self):
        """Gets the database of this VersionOutput.

        Core database version

        :return: The database of this VersionOutput.
        :rtype: int
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this VersionOutput.

        Core database version

        :param database: The database of this VersionOutput.  # noqa: E501
        :type: int
        """

        self._database = database

    @property
    def flywheel_release(self):
        """Gets the flywheel_release of this VersionOutput.

        Flywheel installer image tag as informed by the installation recipe.env

        :return: The flywheel_release of this VersionOutput.
        :rtype: str
        """
        return self._flywheel_release

    @flywheel_release.setter
    def flywheel_release(self, flywheel_release):
        """Sets the flywheel_release of this VersionOutput.

        Flywheel installer image tag as informed by the installation recipe.env

        :param flywheel_release: The flywheel_release of this VersionOutput.  # noqa: E501
        :type: str
        """

        self._flywheel_release = flywheel_release

    @property
    def release(self):
        """Gets the release of this VersionOutput.

        Core release version

        :return: The release of this VersionOutput.
        :rtype: str
        """
        return self._release

    @release.setter
    def release(self, release):
        """Sets the release of this VersionOutput.

        Core release version

        :param release: The release of this VersionOutput.  # noqa: E501
        :type: str
        """

        self._release = release


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
        if not isinstance(other, VersionOutput):
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
