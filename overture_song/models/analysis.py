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


class Analysis(object):
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
        'analysis_state': 'str',
        'analysis_type': 'AnalysisTypeId',
        'files': 'list[FileEntity]',
        'samples': 'list[CompositeEntity]',
        'study_id': 'str'
    }

    attribute_map = {
        'analysis_id': 'analysisId',
        'analysis_state': 'analysisState',
        'analysis_type': 'analysisType',
        'files': 'files',
        'samples': 'samples',
        'study_id': 'studyId'
    }

    def __init__(self, analysis_id=None, analysis_state=None, analysis_type=None, files=None, samples=None, study_id=None):  # noqa: E501
        """Analysis - a model defined in Swagger"""  # noqa: E501

        self._analysis_id = None
        self._analysis_state = None
        self._analysis_type = None
        self._files = None
        self._samples = None
        self._study_id = None
        self.discriminator = None

        if analysis_id is not None:
            self.analysis_id = analysis_id
        if analysis_state is not None:
            self.analysis_state = analysis_state
        if analysis_type is not None:
            self.analysis_type = analysis_type
        if files is not None:
            self.files = files
        if samples is not None:
            self.samples = samples
        if study_id is not None:
            self.study_id = study_id

    @property
    def analysis_id(self):
        """Gets the analysis_id of this Analysis.  # noqa: E501


        :return: The analysis_id of this Analysis.  # noqa: E501
        :rtype: str
        """
        return self._analysis_id

    @analysis_id.setter
    def analysis_id(self, analysis_id):
        """Sets the analysis_id of this Analysis.


        :param analysis_id: The analysis_id of this Analysis.  # noqa: E501
        :type: str
        """

        self._analysis_id = analysis_id

    @property
    def analysis_state(self):
        """Gets the analysis_state of this Analysis.  # noqa: E501


        :return: The analysis_state of this Analysis.  # noqa: E501
        :rtype: str
        """
        return self._analysis_state

    @analysis_state.setter
    def analysis_state(self, analysis_state):
        """Sets the analysis_state of this Analysis.


        :param analysis_state: The analysis_state of this Analysis.  # noqa: E501
        :type: str
        """

        self._analysis_state = analysis_state

    @property
    def analysis_type(self):
        """Gets the analysis_type of this Analysis.  # noqa: E501


        :return: The analysis_type of this Analysis.  # noqa: E501
        :rtype: AnalysisTypeId
        """
        return self._analysis_type

    @analysis_type.setter
    def analysis_type(self, analysis_type):
        """Sets the analysis_type of this Analysis.


        :param analysis_type: The analysis_type of this Analysis.  # noqa: E501
        :type: AnalysisTypeId
        """

        self._analysis_type = analysis_type

    @property
    def files(self):
        """Gets the files of this Analysis.  # noqa: E501


        :return: The files of this Analysis.  # noqa: E501
        :rtype: list[FileEntity]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Analysis.


        :param files: The files of this Analysis.  # noqa: E501
        :type: list[FileEntity]
        """

        self._files = files

    @property
    def samples(self):
        """Gets the samples of this Analysis.  # noqa: E501


        :return: The samples of this Analysis.  # noqa: E501
        :rtype: list[CompositeEntity]
        """
        return self._samples

    @samples.setter
    def samples(self, samples):
        """Sets the samples of this Analysis.


        :param samples: The samples of this Analysis.  # noqa: E501
        :type: list[CompositeEntity]
        """

        self._samples = samples

    @property
    def study_id(self):
        """Gets the study_id of this Analysis.  # noqa: E501


        :return: The study_id of this Analysis.  # noqa: E501
        :rtype: str
        """
        return self._study_id

    @study_id.setter
    def study_id(self, study_id):
        """Sets the study_id of this Analysis.


        :param study_id: The study_id of this Analysis.  # noqa: E501
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
        if issubclass(Analysis, dict):
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
        if not isinstance(other, Analysis):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
