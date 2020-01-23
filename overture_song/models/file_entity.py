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


class FileEntity(object):
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
        'analysis_id': 'str',
        'data_type': 'str',
        'file_access': 'str',
        'file_md5sum': 'str',
        'file_name': 'str',
        'file_size': 'int',
        'file_type': 'str',
        'info': 'JsonNode',
        'object_id': 'str',
        'study_id': 'str'
    }

    attribute_map = {
        'analysis_id': 'analysisId',
        'data_type': 'dataType',
        'file_access': 'fileAccess',
        'file_md5sum': 'fileMd5sum',
        'file_name': 'fileName',
        'file_size': 'fileSize',
        'file_type': 'fileType',
        'info': 'info',
        'object_id': 'objectId',
        'study_id': 'studyId'
    }

    def __init__(self, analysis_id=None, data_type=None, file_access=None, file_md5sum=None, file_name=None, file_size=None, file_type=None, info=None, object_id=None, study_id=None):  # noqa: E501
        """FileEntity - a model defined in Swagger"""  # noqa: E501

        self._analysis_id = None
        self._data_type = None
        self._file_access = None
        self._file_md5sum = None
        self._file_name = None
        self._file_size = None
        self._file_type = None
        self._info = None
        self._object_id = None
        self._study_id = None
        self.discriminator = None

        if analysis_id is not None:
            self.analysis_id = analysis_id
        if data_type is not None:
            self.data_type = data_type
        if file_access is not None:
            self.file_access = file_access
        if file_md5sum is not None:
            self.file_md5sum = file_md5sum
        if file_name is not None:
            self.file_name = file_name
        if file_size is not None:
            self.file_size = file_size
        if file_type is not None:
            self.file_type = file_type
        if info is not None:
            self.info = info
        if object_id is not None:
            self.object_id = object_id
        if study_id is not None:
            self.study_id = study_id

    @property
    def analysis_id(self):
        """Gets the analysis_id of this FileEntity.  # noqa: E501


        :return: The analysis_id of this FileEntity.  # noqa: E501
        :rtype: str
        """
        return self._analysis_id

    @analysis_id.setter
    def analysis_id(self, analysis_id):
        """Sets the analysis_id of this FileEntity.


        :param analysis_id: The analysis_id of this FileEntity.  # noqa: E501
        :type: str
        """

        self._analysis_id = analysis_id

    @property
    def data_type(self):
        """Gets the data_type of this FileEntity.  # noqa: E501


        :return: The data_type of this FileEntity.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this FileEntity.


        :param data_type: The data_type of this FileEntity.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def file_access(self):
        """Gets the file_access of this FileEntity.  # noqa: E501


        :return: The file_access of this FileEntity.  # noqa: E501
        :rtype: str
        """
        return self._file_access

    @file_access.setter
    def file_access(self, file_access):
        """Sets the file_access of this FileEntity.


        :param file_access: The file_access of this FileEntity.  # noqa: E501
        :type: str
        """

        self._file_access = file_access

    @property
    def file_md5sum(self):
        """Gets the file_md5sum of this FileEntity.  # noqa: E501


        :return: The file_md5sum of this FileEntity.  # noqa: E501
        :rtype: str
        """
        return self._file_md5sum

    @file_md5sum.setter
    def file_md5sum(self, file_md5sum):
        """Sets the file_md5sum of this FileEntity.


        :param file_md5sum: The file_md5sum of this FileEntity.  # noqa: E501
        :type: str
        """

        self._file_md5sum = file_md5sum

    @property
    def file_name(self):
        """Gets the file_name of this FileEntity.  # noqa: E501


        :return: The file_name of this FileEntity.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this FileEntity.


        :param file_name: The file_name of this FileEntity.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def file_size(self):
        """Gets the file_size of this FileEntity.  # noqa: E501


        :return: The file_size of this FileEntity.  # noqa: E501
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this FileEntity.


        :param file_size: The file_size of this FileEntity.  # noqa: E501
        :type: int
        """

        self._file_size = file_size

    @property
    def file_type(self):
        """Gets the file_type of this FileEntity.  # noqa: E501


        :return: The file_type of this FileEntity.  # noqa: E501
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this FileEntity.


        :param file_type: The file_type of this FileEntity.  # noqa: E501
        :type: str
        """

        self._file_type = file_type

    @property
    def info(self):
        """Gets the info of this FileEntity.  # noqa: E501


        :return: The info of this FileEntity.  # noqa: E501
        :rtype: JsonNode
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this FileEntity.


        :param info: The info of this FileEntity.  # noqa: E501
        :type: JsonNode
        """

        self._info = info

    @property
    def object_id(self):
        """Gets the object_id of this FileEntity.  # noqa: E501


        :return: The object_id of this FileEntity.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this FileEntity.


        :param object_id: The object_id of this FileEntity.  # noqa: E501
        :type: str
        """

        self._object_id = object_id

    @property
    def study_id(self):
        """Gets the study_id of this FileEntity.  # noqa: E501


        :return: The study_id of this FileEntity.  # noqa: E501
        :rtype: str
        """
        return self._study_id

    @study_id.setter
    def study_id(self, study_id):
        """Sets the study_id of this FileEntity.


        :param study_id: The study_id of this FileEntity.  # noqa: E501
        :type: str
        """

        self._study_id = study_id

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
        if issubclass(FileEntity, dict):
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
        if not isinstance(other, FileEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
