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


class RegisterAnalysisTypeRequest(object):
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
        'name': 'str',
        'schema': 'JsonNode'
    }

    attribute_map = {
        'name': 'name',
        'schema': 'schema'
    }

    def __init__(self, name=None, schema=None):  # noqa: E501
        """RegisterAnalysisTypeRequest - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._schema = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if schema is not None:
            self.schema = schema

    @property
    def name(self):
        """Gets the name of this RegisterAnalysisTypeRequest.  # noqa: E501


        :return: The name of this RegisterAnalysisTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RegisterAnalysisTypeRequest.


        :param name: The name of this RegisterAnalysisTypeRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def schema(self):
        """Gets the schema of this RegisterAnalysisTypeRequest.  # noqa: E501


        :return: The schema of this RegisterAnalysisTypeRequest.  # noqa: E501
        :rtype: JsonNode
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this RegisterAnalysisTypeRequest.


        :param schema: The schema of this RegisterAnalysisTypeRequest.  # noqa: E501
        :type: JsonNode
        """

        self._schema = schema

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
        if issubclass(RegisterAnalysisTypeRequest, dict):
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
        if not isinstance(other, RegisterAnalysisTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
