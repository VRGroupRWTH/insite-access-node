# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from access_node.models.base_model_ import Model
from access_node import util


class SimulationTimeInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, start: float=None, end: float=None, current: float=None):  # noqa: E501
        """SimulationTimeInfo - a model defined in Swagger

        :param start: The start of this SimulationTimeInfo.  # noqa: E501
        :type start: float
        :param end: The end of this SimulationTimeInfo.  # noqa: E501
        :type end: float
        :param current: The current of this SimulationTimeInfo.  # noqa: E501
        :type current: float
        """
        self.swagger_types = {
            'start': float,
            'end': float,
            'current': float
        }

        self.attribute_map = {
            'start': 'start',
            'end': 'end',
            'current': 'current'
        }

        self._start = start
        self._end = end
        self._current = current

    @classmethod
    def from_dict(cls, dikt) -> 'SimulationTimeInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SimulationTimeInfo of this SimulationTimeInfo.  # noqa: E501
        :rtype: SimulationTimeInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def start(self) -> float:
        """Gets the start of this SimulationTimeInfo.


        :return: The start of this SimulationTimeInfo.
        :rtype: float
        """
        return self._start

    @start.setter
    def start(self, start: float):
        """Sets the start of this SimulationTimeInfo.


        :param start: The start of this SimulationTimeInfo.
        :type start: float
        """

        self._start = start

    @property
    def end(self) -> float:
        """Gets the end of this SimulationTimeInfo.


        :return: The end of this SimulationTimeInfo.
        :rtype: float
        """
        return self._end

    @end.setter
    def end(self, end: float):
        """Sets the end of this SimulationTimeInfo.


        :param end: The end of this SimulationTimeInfo.
        :type end: float
        """

        self._end = end

    @property
    def current(self) -> float:
        """Gets the current of this SimulationTimeInfo.


        :return: The current of this SimulationTimeInfo.
        :rtype: float
        """
        return self._current

    @current.setter
    def current(self, current: float):
        """Sets the current of this SimulationTimeInfo.


        :param current: The current of this SimulationTimeInfo.
        :type current: float
        """

        self._current = current
