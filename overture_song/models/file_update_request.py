# coding: utf-8

"""
    Song API

    Song API reference for developers. SONG is an open source system for validating and tracking metadata about raw data submissions, assigning identifiers to entities of interest, and managing the state of the raw data with regards to publication and access  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FileUpdateRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'file_access': 'str',
        'file_md5sum': 'str',
        'file_size': 'int',
        'info': 'JsonNode'
    }

    attribute_map = {
        'file_access': 'fileAccess',
        'file_md5sum': 'fileMd5sum',
        'file_size': 'fileSize',
        'info': 'info'
    }

    def __init__(self, file_access=None, file_md5sum=None, file_size=None, info=None):  # noqa: E501
        """FileUpdateRequest - a model defined in Swagger"""  # noqa: E501

        self._file_access = None
        self._file_md5sum = None
        self._file_size = None
        self._info = None
        self.discriminator = None

        if file_access is not None:
            self.file_access = file_access
        if file_md5sum is not None:
            self.file_md5sum = file_md5sum
        if file_size is not None:
            self.file_size = file_size
        if info is not None:
            self.info = info

    @property
    def file_access(self):
        """Gets the file_access of this FileUpdateRequest.  # noqa: E501


        :return: The file_access of this FileUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._file_access

    @file_access.setter
    def file_access(self, file_access):
        """Sets the file_access of this FileUpdateRequest.


        :param file_access: The file_access of this FileUpdateRequest.  # noqa: E501
        :type: str
        """

        self._file_access = file_access

    @property
    def file_md5sum(self):
        """Gets the file_md5sum of this FileUpdateRequest.  # noqa: E501


        :return: The file_md5sum of this FileUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._file_md5sum

    @file_md5sum.setter
    def file_md5sum(self, file_md5sum):
        """Sets the file_md5sum of this FileUpdateRequest.


        :param file_md5sum: The file_md5sum of this FileUpdateRequest.  # noqa: E501
        :type: str
        """

        self._file_md5sum = file_md5sum

    @property
    def file_size(self):
        """Gets the file_size of this FileUpdateRequest.  # noqa: E501


        :return: The file_size of this FileUpdateRequest.  # noqa: E501
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this FileUpdateRequest.


        :param file_size: The file_size of this FileUpdateRequest.  # noqa: E501
        :type: int
        """

        self._file_size = file_size

    @property
    def info(self):
        """Gets the info of this FileUpdateRequest.  # noqa: E501


        :return: The info of this FileUpdateRequest.  # noqa: E501
        :rtype: JsonNode
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this FileUpdateRequest.


        :param info: The info of this FileUpdateRequest.  # noqa: E501
        :type: JsonNode
        """

        self._info = info

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
        if issubclass(FileUpdateRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FileUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
