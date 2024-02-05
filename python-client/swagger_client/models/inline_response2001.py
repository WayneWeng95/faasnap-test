# coding: utf-8

"""
    faasnap

    FaaSnap API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class InlineResponse2001(object):
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
        'duration': 'float',
        'result': 'str',
        'vm_id': 'str',
        'trace_id': 'str'
    }

    attribute_map = {
        'duration': 'duration',
        'result': 'result',
        'vm_id': 'vmId',
        'trace_id': 'traceId'
    }

    def __init__(self, duration=None, result=None, vm_id=None, trace_id=None, _configuration=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._duration = None
        self._result = None
        self._vm_id = None
        self._trace_id = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if result is not None:
            self.result = result
        if vm_id is not None:
            self.vm_id = vm_id
        if trace_id is not None:
            self.trace_id = trace_id

    @property
    def duration(self):
        """Gets the duration of this InlineResponse2001.  # noqa: E501


        :return: The duration of this InlineResponse2001.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InlineResponse2001.


        :param duration: The duration of this InlineResponse2001.  # noqa: E501
        :type: float
        """

        self._duration = duration

    @property
    def result(self):
        """Gets the result of this InlineResponse2001.  # noqa: E501


        :return: The result of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this InlineResponse2001.


        :param result: The result of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._result = result

    @property
    def vm_id(self):
        """Gets the vm_id of this InlineResponse2001.  # noqa: E501


        :return: The vm_id of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        """Sets the vm_id of this InlineResponse2001.


        :param vm_id: The vm_id of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._vm_id = vm_id

    @property
    def trace_id(self):
        """Gets the trace_id of this InlineResponse2001.  # noqa: E501


        :return: The trace_id of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        """Sets the trace_id of this InlineResponse2001.


        :param trace_id: The trace_id of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._trace_id = trace_id

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
        if issubclass(InlineResponse2001, dict):
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
        if not isinstance(other, InlineResponse2001):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2001):
            return True

        return self.to_dict() != other.to_dict()
